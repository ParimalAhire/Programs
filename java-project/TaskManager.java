import java.util.ArrayList;
import java.util.Scanner;
import java.io.*;

class Task {
    String description;
    String deadline;
    boolean isCompleted;

    Task(String description, String deadline) {
        this.description = description;
        this.deadline = deadline;
        this.isCompleted = false;
    }

    @Override
    public String toString() {
        return (isCompleted ? "[Completed] " : "[Pending] ") + description + " (Deadline: " + deadline + ")";
    }
}

public class TaskManager {
    private static ArrayList<Task> tasks = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        loadTasks();

        while (true) {
            System.out.println("Task Manager");
            System.out.println("1. Add Task");
            System.out.println("2. View Tasks");
            System.out.println("3. Mark Task as Completed");
            System.out.println("4. Save and Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter task description: ");
                    String description = scanner.nextLine();
                    System.out.print("Enter task deadline: ");
                    String deadline = scanner.nextLine();
                    tasks.add(new Task(description, deadline));
                    break;
                case 2:
                    for (int i = 0; i < tasks.size(); i++) {
                        System.out.println((i + 1) + ". " + tasks.get(i));
                    }
                    break;
                case 3:
                    System.out.print("Enter task number to mark as completed: ");
                    int taskNumber = scanner.nextInt();
                    if (taskNumber > 0 && taskNumber <= tasks.size()) {
                        tasks.get(taskNumber - 1).isCompleted = true;
                    } else {
                        System.out.println("Invalid task number.");
                    }
                    break;
                case 4:
                    saveTasks();
                    System.out.println("Tasks saved. Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid option.");
            }
        }
    }

    private static void saveTasks() {
        try (PrintWriter writer = new PrintWriter(new FileWriter("tasks.txt"))) {
            for (Task task : tasks) {
                writer.println(task.description + "|" + task.deadline + "|" + task.isCompleted);
            }
        } catch (IOException e) {
            System.out.println("Error saving tasks.");
        }
    }

    private static void loadTasks() {
        try (BufferedReader reader = new BufferedReader(new FileReader("tasks.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split("\\|");
                if (parts.length == 3) {
                    Task task = new Task(parts[0], parts[1]);
                    task.isCompleted = Boolean.parseBoolean(parts[2]);
                    tasks.add(task);
                }
            }
        } catch (IOException e) {
            System.out.println("Error loading tasks.");
        }
    }
}
