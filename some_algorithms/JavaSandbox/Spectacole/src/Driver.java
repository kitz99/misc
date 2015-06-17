import java.util.*;
public class Driver {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("N=");
		int n = sc.nextInt();
		LinkedList<Interval> list = new LinkedList<Interval>();
		for(int i = 1; i <=  n; i++){
			int start = sc.nextInt();
			int end = sc.nextInt();
			list.add(new Interval(start, end));
		}
		sc.close();
		
		Collections.sort(list);
		
		LinkedList<LinkedList<Interval>> multimi = new LinkedList<>();
		
		while(!list.isEmpty()){
			boolean g = false;
			for(LinkedList<Interval>m_crt : multimi){
				if(m_crt.getLast().end <= list.getFirst().start){
					m_crt.add(list.getFirst());
					g = true;
					break;
				}
			}
			if(!g){
				multimi.add(new LinkedList<Interval>());
				multimi.getLast().add(list.getFirst());
			}
			list.removeFirst();
		}
		
		for(LinkedList<Interval>m_crt : multimi){
			System.out.println(m_crt);
		}
	}

}
