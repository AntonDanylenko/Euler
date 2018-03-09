public class Euler{
    public static int prob1(int maxVal){
	int result = 0;
	for (int n=1; n<maxVal; n++){
	    if (n%3 == 0 || n%5 == 0){
		result += n;
	    }
	}
	return result;
    }



    public static int prob2(int maxVal){
	int result = 0;
	int m = 0;
	int n = 1;
	while (n<maxVal){
	    if (n%2 == 0){
		result += n;
	    }
	    int temp = n;
	    n += m;
	    m = temp;
	}
	return result;
    }



    public static int prob3(int Val){
	int result = 0;
	int newNum = Val;
	int maxPrime = 2;
	int prime = 2;
	while (newNum>1){
	    newNum = newNum/prime;
	    //prime += ?;
	}
	return maxPrime;
    }	    



    public static void main(String[]args){
	//System.out.println("problem1: " + prob1(1000));
	//System.out.println("problem2: " + prob2(4000000));
	System.out.println("problem3: " + prob3(600851475143));
    }
}
