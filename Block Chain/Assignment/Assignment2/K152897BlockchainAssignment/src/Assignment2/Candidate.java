package Assignment2;
import Assignment2.Transaction;

public class Candidate {
	Transaction tx;
	int sender;
	
	public Candidate(Transaction tx, int sender) {
		this.tx = tx;
		this.sender = sender;
	}

	public int getSender() {
		return sender;
	}
}