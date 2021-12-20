package Coursework;
import java.util.Scanner;
public class ConsoleHelper {

    public int getInt(String prompt){
        Scanner in = new Scanner(System.in);
        int i;
        System.out.println(prompt);
        try{ i = in.nextInt(); }
        catch (Exception e){ return getInt(prompt); }
        return i;
    }
    public String getString(String prompt) {
        Scanner in = new Scanner(System.in);
        String s;
        System.out.println(prompt);
        s = in.nextLine();
        return s;
    }
    public void out(String message) { System.out.println(message); }

    public void menuOptions(SmartHome Home) {
        out("                  -----------------MENU OPTIONS-----------------                    ");
        out("                  -----------------Please Select An Option-----------------                    ");
        out("""
                1 - House Level Options
                2 - Room Level Options
                3 - Plug Level Options
                4 - System Options""");
        out("-----------------------------------------------------------------------");
        int optionLevelChoice = getInt("");
        switch (optionLevelChoice) {
            case 1 -> {
                out("HOUSE LEVEL OPTIONS");
                out("""
                        1 - Switch All Plugs Off
                        2 - Switch All Plugs On
                        Select an Option""");
                int houseLevelDecision = getInt("");
                Home.houseToggle(houseLevelDecision); }

            case 2 -> {
                System.out.println(Home.roomList());
                out("PLEASE SELECT A ROOM(integer only)");
                int roomChoiceNumber = getInt("");
                System.out.println(Home.roomChoiceOptions());
                int roomPlugOptionChoice = getInt("");
                Home.roomOptions(roomChoiceNumber, roomPlugOptionChoice);
                if (roomPlugOptionChoice == 3) {
                    System.out.println(Home.roomOptionsChoice3List(roomChoiceNumber, roomPlugOptionChoice));
                    int deviceChoiceNumber = getInt("Using the above list, Please select the plug Location ( Final integer only): ");
                    System.out.println(Home.roomOptionsChoice3(roomChoiceNumber, roomPlugOptionChoice, deviceChoiceNumber));

                } }

            case 3 -> {
                System.out.println(Home.plugList());
                int plugChoiceNumber = getInt("");

                System.out.println(Home.plugOptions(plugChoiceNumber));
                int plugOnOff = getInt("");

                Home.plugDeviceOptions(plugChoiceNumber, plugOnOff);

                if (plugOnOff == 3) {
                    System.out.println(Home.plugDeviceOptionsChoice3(plugChoiceNumber, plugOnOff));
                    int plugDevice = getInt("");
                    Home.plugOptionsChangeDevice(plugChoiceNumber, plugOnOff, plugDevice);
                }

                if (plugOnOff == 4) {
                    System.out.println(Home.plugDeviceChangeLocation(plugChoiceNumber, plugOnOff));
                    int new_room = getInt("");
                    Home.plugDeviceChoice4RoomLocation(plugChoiceNumber, plugOnOff, new_room);
                }

            }
            case 4 -> {
                System.out.println(Home.system_list());
                int Option = getInt("");
                switch (Option) {
                    case 1 -> {
                        System.out.println(Home.plugInformation());

                        int roomChoiceNumber = getInt("Using the above list, Please select the room for this plug (integer only): ");

                        System.out.println(Home.displayDeviceList());
                        int deviceChoiceNumber = getInt("Using the above list, Please select the Device for this plug (integer only): ");

                        Home.plugMaker(deviceChoiceNumber, roomChoiceNumber);
                    }
                    case 2 -> {
                        System.out.println("Please enter new Device");
                        String newDeviceName = getString("");
                        Home.addNewDevice(newDeviceName);
                    }
                    case 3 -> {
                        System.out.println("Please enter New Room");
                        String newRoomName = getString("");
                        Home.appendRoom(newRoomName);
                    }
                }
            }
            default -> out("please enter a valid option");
        }
    }
}
