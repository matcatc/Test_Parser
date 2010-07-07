import junit.framework.*;

public class JUnit3_test extends TestCase {

	// Normally you would be testing some function's output, and not some variable you set...
	public void testOne() {
		int a = 2;
		int b = 2;
		int sum = a + b;
		int expected = 4;
		assertEquals(sum, expected); // 2 + 2 = 4?
	}

	//This test should fail...
	public void testTwo() {
		int a = 2;
		int b = 2;
		int sum = a + b +1; // Just pretend that "+1" was a mistake you overlooked
		int expected = 4;
		assertEquals(sum, expected); // 2 + 2 = 5?
	}
}

