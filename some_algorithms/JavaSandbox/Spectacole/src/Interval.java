
public class Interval implements Comparable<Interval>{
	int start;
	int end;
	public Interval(int start, int end){
		this.start = start;
		this.end = end;
	}
	@Override
	public int compareTo(Interval that) {
		return this.start - that.start;
	}
	@Override
	public String toString(){
		return "["+this.start+ " , " + this.end + "] ";
	}
}
