import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Junit4_test{

	@Test
	public void testOne() {
		int a = 2;
		int b = 2;
		int sum = a + b;
		int expected = 4;
		assertEquals(sum, expected); // 2 + 2 = 4?
	}

	@Test
	public void testTwo() {
		int a = 2;
		int b = 2;
		int sum = a + b +1;
		int expected = 4;
		assertEquals(sum, expected); // 2 + 2 = 5?
	}
}

