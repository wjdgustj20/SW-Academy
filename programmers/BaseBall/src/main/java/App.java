import engine.BaseBall;
import engine.io.NumberGenerator;

public class App {
    public static void main(String[] args) {

        NumberGenerator generator = new HackFakerNumberGenerator();
        Console console = new Console();

        new BaseBall(generator, console, console).run();
    }
}
