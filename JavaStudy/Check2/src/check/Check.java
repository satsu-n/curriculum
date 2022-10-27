package check;

import constants.Constants;

public class Check {
	private static final String firstName = "niiya";
	private static final String lastName = "satsuka";

	
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		
		printName(firstName,lastName);
		
		String java = Constants.CHECK_CLASS_JAVA;
		String hoge = Constants.CHECK_CLASS_HOGE;
		String r2d2 = Constants.CHECK_CLASS_R2D2;
		String luke = Constants.CHECK_CLASS_LUKE;
		
		Pet master = new Pet(java,hoge);
		master.introduce();
		
		RobotPet robot = new RobotPet(r2d2,luke);
		robot.introduce();
		
	}
	private static void printName(String first,String last) {
		
        System.out.println("printNameメソッド → " + first + last);

	}

}
