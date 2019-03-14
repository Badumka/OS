class DemoThread implements Runnable {
    DemoThread() {
        Thread m = Thread.currentThread(); // Помещается основной поток в переменную m
        Thread t = new Thread(this, "Demo Thread"); // Создаётся дочерний поток в t
        t.start(); // Запускается поток t
        try {
            Thread.sleep(5000); // Созданный поток переводим в режим ожидания на 5 секунд
        } catch (InterruptedException e) {
        }
    }
    public void run() { //выполняет простой метод после которого завершится поток
        try {
            for (int i = 5; i > 0; i--) {
                System.out.println("" + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
        }
    }
    public static void main(String args[]) { //вызывает дочерний процесс
        new DemoThread();
    }
}