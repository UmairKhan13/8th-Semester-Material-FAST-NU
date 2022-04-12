package Assignment2;

import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/* CompliantNode refers to a node that follows the rules (not malicious)*/
public class CompliantNode implements Node {

    public double p_graph;
    public double p_malicious;
    public double p_txDistribution;
    public int numRounds;
    public boolean[] followees;
    public Set<Transaction> pendingTransactions;
    public boolean[] isNotFollowees;
    public Set<Transaction> currentTransactions;
    public int tempInt1 =0;
    public int tempInt2 =0;


    public CompliantNode(double p_graph, double p_malicious, double p_txDistribution, int numRounds) {
        this.p_graph = p_graph;
        this.p_malicious = p_malicious;
        this.p_txDistribution = p_txDistribution;
        this.numRounds = numRounds;
    }

    public void setFollowees(boolean[] followees) {
        this.followees = followees;
        isNotFollowees = new boolean[followees.length];
        for(int i = 0; i< isNotFollowees.length; i++)
        {
            isNotFollowees[i]= false;
        }
    }

    public void setPendingTransaction(Set<Transaction> pendingTransactions) {
        this.pendingTransactions = pendingTransactions;
        this.currentTransactions = pendingTransactions;
    }

    public Set<Transaction> sendToFollowers() {
        Set<Transaction> Txs = new HashSet<>();
        if(tempInt1 < numRounds)
        {
            for(Transaction t : pendingTransactions)
            {
                Txs.add(t);
            }
            tempInt2 = tempInt1;
        }
        else if(tempInt1 == numRounds)
        {
            Txs = currentTransactions;
        }
        return Txs;
    }

    public void receiveFromFollowees(Set<Candidate> candidates) {
        if(tempInt1>=numRounds)
        {
            return;
        }
        else if(tempInt2 > 0 && tempInt1 > tempInt2)
        {
            pendingTransactions.clear();
        }

        Set<Integer> senders = new HashSet<>();
//        Set<Integer> senders = candidates.stream().map(c -> c.sender).collect(Collectors.toSet());
        for(Candidate c : candidates)
        {
            senders.add(c.sender);
        }

        for(int i=0; i<followees.length; i++)
        {
            if(senders.contains(i) && followees[i])
                isNotFollowees[i] = true;
        }

        for(Candidate c: candidates)
        {
            if(!(currentTransactions.contains(c.tx) || isNotFollowees[c.sender]))
            {
                currentTransactions.add(c.tx);
                pendingTransactions.add(c.tx);
                System.out.println("Transaction added: " + c.tx);
            }
            else
                System.out.println("Trasaction # " + c.tx + " is Malicious...");
        }
    }
}
