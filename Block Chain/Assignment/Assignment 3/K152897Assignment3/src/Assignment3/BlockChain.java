package Assignment3;// blockchain.assignment3.Block Chain should maintain only limited block nodes to satisfy the functions
// You should not have all the blocks added to the block chain in memory
// as it would cause a memory overflow.

import java.util.ArrayList;
import java.util.HashMap;

public class BlockChain {
    public static final int CUT_OFF_AGE = 10;

    //default private
    class BlockChainMapping
    {
        public BlockChainMapping head;
        public BlockChainMapping tail;
        public Block mappingBlock;
        public ArrayList<BlockChainMapping> tailList;
        public int headSize;
        public UTXOPool utxoPool;

        public BlockChainMapping(BlockChainMapping head, BlockChainMapping tail, Block mappingBlock, UTXOPool utxoPool) {
            this.head = head;
            this.tail = tail;
            this.mappingBlock = mappingBlock;
            this.tailList = new ArrayList<>();
            this.utxoPool = utxoPool;
            setHeadSize(head);
        }

        //no default Constructor

        public UTXOPool getUtxoPool() {
            return new UTXOPool(utxoPool);
        }

        public BlockChainMapping getHead() {
            return head;
        }

        public void setHeadSize(BlockChainMapping headTemp) {

            if(headTemp == null)
                headSize = 1;
            else
            {
                headSize = headTemp.headSize;
                headSize++;
                headTemp.tailList.add(this);
            }
        }

    }

    /**
     * create an empty block chain with just a genesis block. Assume {@code genesisBlock} is a valid
     * block
     */
    UTXOPool utxoInitial;
    TxHandler tempTxHandler;


    /*Required for: Maintain only one global Transaction Pool
    for the block chain and keep adding transactions to it on
    receiving transactions and remove transactions from it if
     a new block is received or created.*/
    public static TransactionPool transactionPool = new TransactionPool();


    public  BlockChainMapping maxHeightMapped = null;
    public HashMap<ByteArrayWrapper, BlockChainMapping> blockChain;


    public BlockChain(Block genesisBlock) {
        //getGenesisBlock


        utxoInitial =new UTXOPool();
        Transaction genesisTrasaction = getCoinBaseTransactionOfUtxo(genesisBlock);
        insertIntoUtxoPool(utxoInitial, genesisTrasaction);

        BlockChainMapping genesisMapping = new BlockChainMapping(null, null, genesisBlock, utxoInitial);
        maxHeightMapped= genesisMapping;
        blockChain = new HashMap<>();
        if(genesisBlock != null)
        blockChain.put(getBytesArr(genesisBlock.getHash()), genesisMapping);

    }

    /** Get the maximum height block */
    public Block getMaxHeightBlock() {
        return maxHeightMapped.mappingBlock;
    }

    /** Get the blockchain.assignment3.UTXOPool for mining a new block on top of max height block */
    public UTXOPool getMaxHeightUTXOPool() {
        return new UTXOPool(maxHeightMapped.utxoPool);
    }

    /** Get the transaction pool to mine a new block */
    public TransactionPool getTransactionPool() {
        return transactionPool;
    }

    /**
     * Add {@code block} to the block chain if it is valid. For validity, all transactions should be
     * valid and block should be at {@code height > (maxHeight - CUT_OFF_AGE)}.
     *
     * <p>
     * For example, you can try creating a new block over the genesis block (block height 2) if the
     * block chain height is {@code <=
     * CUT_OFF_AGE + 1}. As soon as {@code height > CUT_OFF_AGE + 1}, you cannot create a new block
     * at height 2.
     *
     * @return true if block is successfully added
     */
    public boolean addBlock(Block block) {

        //getBlock
        byte [] prehash = block.getPrevBlockHash();
        if(prehash == null)
            return false;
        BlockChainMapping preMapping= blockChain.get(getBytesArr(prehash));

        if(checkConnectedMapping(block , preMapping)) {
            if(!getTrasactionResponse(preMapping, block))
            {
                return false;
            }
            else {
                if ((preMapping.headSize + 1) < maxHeightMapped.headSize - CUT_OFF_AGE) {
                    return false;
                }
                else
                {   UTXOPool utxoStorage = tempTxHandler.getUTXOPool();
                    insertIntoUtxoPool(utxoStorage ,getCoinBaseTransactionOfUtxo(block));
                    BlockChainMapping bcm = new BlockChainMapping(preMapping, null, block, utxoStorage);
                    blockChain.put(getBytesArr(block.getHash()) , bcm);
                    manageHeight(preMapping, bcm);
                }
            }
            return true;
        }
        else
        {
            System.out.println("can't connect to parent mapping");
            return false;
        }

    }

    /** Add a transaction to the transaction pool */
    public void addTransaction(Transaction tx) {
        transactionPool.addTransaction(tx);
    }

    public BlockChainMapping getMaxHeightMapped() {
        return maxHeightMapped;
    }

    public void setMaxHeightMapped(BlockChainMapping maxHeightMapped) {
        this.maxHeightMapped = maxHeightMapped;
    }

    public boolean insertIntoUtxoPool(UTXOPool up, Transaction t)
    {

        for (int count = 0; count < t.numOutputs(); count++) {
            byte[] transactionHash = t.getHash();
            UTXO utxoTemp = new UTXO(transactionHash, count);
            Transaction.Output output = t.getOutput(count);
            up.addUTXO(utxoTemp, output);
        }
        return true;
    }

    public Transaction getCoinBaseTransactionOfUtxo(Block block)
    {
        return block.getCoinbase();
    }

    public boolean checkConnectedMapping(Block b , BlockChainMapping bcm)
    {
        if(b.getPrevBlockHash() == null || bcm == null)
        {
            return false;
        }
        return true;
    }

    public ByteArrayWrapper getBytesArr(byte [] arr)
    {
        return new ByteArrayWrapper(arr);

    }

    public boolean getTrasactionResponse(BlockChainMapping blockChainMapping, Block block)
    {
        UTXOPool utxoCopy = new UTXOPool(blockChainMapping.getUtxoPool());
        TxHandler txHandler = new TxHandler(utxoCopy);
        Transaction[] transactions = block.getTransactions().toArray(new Transaction[0]);
        Transaction[] secureTransactions = txHandler.handleTxs(transactions);

        if(secureTransactions.length != transactions.length)
            return false;
        else
        {
            tempTxHandler = txHandler;
            return true;
        }
    }

    public boolean manageHeight(BlockChainMapping preMapping, BlockChainMapping bcm)
    {
        if((preMapping.headSize + 1) > maxHeightMapped.headSize)
        {
            maxHeightMapped = bcm;
            return true;
        }
        return false;
    }
}