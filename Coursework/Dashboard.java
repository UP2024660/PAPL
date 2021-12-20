package Coursework;

public class Dashboard {

    public static void main(String[] args){
        ConsoleHelper console = new ConsoleHelper();
        int numberOfRooms = console.getInt("How Many rooms are there in this property?: ");

        int numberOfPlugs = console.getInt("How many plugs are there in this property?: ");

        SmartHome Home = new SmartHome(numberOfRooms,numberOfPlugs);
        Home.addNewDevice("LAMP");
        Home.addNewDevice("TV");
        Home.addNewDevice("COMPUTER");
        Home.addNewDevice("PHONE RECHARGER");
        Home.addNewDevice("HEATER");

        for(int i = 0; i< numberOfRooms; i++) {
            String roomName = console.getString("Enter name for your "+ (i+1)+" room: ");
            Home.appendRoom(roomName);
        }
        for(int i = 0; i< numberOfPlugs; i++) {
            System.out.println(Home.plugInformation());

            int roomChoiceNumber = console.getInt("Using the above list, Please select the room for this plug (integer only): ");

            System.out.println(Home.displayDeviceList());
            int deviceChoiceNumber = console.getInt("Using the above list, Please select the Device for this plug (integer only): ");

            Home.plugMaker(deviceChoiceNumber, roomChoiceNumber);
        }

        while(true){

            console.out(Home.Display());
            console.menuOptions(Home);

        }


    }

}
