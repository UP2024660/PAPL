package Coursework;

public class SmartHome {

    private String[] rooms;
    private SmartPlug[] plugs;
    private String[] deviceNames;
    private int currentIndex;
    private int plugIndex;
    private int deviceIndex;

    public SmartHome(int numberOfRooms, int numberOfPlugs){
        rooms = new String[numberOfRooms];
        plugs = new SmartPlug[numberOfPlugs];
        deviceNames = new String[0];
        currentIndex = 0;
        plugIndex = 0;
        deviceIndex = 0;
    }


    //----------------ROOM_MAKER--------\\
    public void appendRoom(String roomName){
        if (currentIndex >= rooms.length){
            String[] addNewRoom = new String[rooms.length+1];
            for(int i=0; i<rooms.length; i++){ addNewRoom[i] = rooms[i]; }
            rooms = addNewRoom;
        }
        rooms[currentIndex] = roomName;
        currentIndex++;
    }
    //-------------------------------------\\
    //-------------PLUG MAKER--------------\\
    public void plugMaker(int deviceNumber,int roomNumber) {
        String deviceName = deviceNames[deviceNumber-1];
        double plugLocation = locationConverter(roomNumber, deviceNumber);
        String roomName = roomNamer(roomNumber);
        int plugIndex = this.plugIndex + 1;
        SmartPlug Plug = new SmartPlug(false, plugLocation, (plugIndex), deviceName, roomName);
        addNewPlug(Plug);
    }
    //-----------------------------------------\\

    // ----------------- ADD NEW PLUG ----------------- \\
    public void addNewPlug(SmartPlug plug){
        if (plugIndex >= plugs.length){
            SmartPlug[] addNewPlug = new SmartPlug[plugs.length+1];
            for(int i=0; i<plugs.length; i++){ addNewPlug[i] = plugs[i]; }
            plugs = addNewPlug;
        }
        plugs[plugIndex] = plug;
        plugIndex++;
    }
    //-------------------------------------------------------\\

    //------------------- DEVICE MAKER ---------------- \\
    public void addNewDevice(String deviceName){
        if (deviceIndex >= deviceNames.length){
            String[] addNewDevice = new String[deviceNames.length+1];
            for(int i=0; i<deviceNames.length; i++){ addNewDevice[i] = deviceNames[i]; }
            deviceNames = addNewDevice;
        }
        deviceNames[deviceIndex] = deviceName;
        deviceIndex++;
    }
    //----------------------------------------------------\\

    //------------------------------ PLUG FUNCTIONS ------------ \\
    public String plugInformation() {
        StringBuilder output = new StringBuilder();
        output.append("ENTER PLUG INFORMATION BELOW:\n");
        output.append("ROOMS AVAILABLE:\n");
        for (int a = 0; a < rooms.length; a++) {
            output.append("\n").append(a + 1).append(" -  ").append(rooms[a]).append("\n"); }
        return output.toString();
    }

    public String plugList(){
        StringBuilder output = new StringBuilder();
        output.append("PLUGS AVAILABLE:\n");
        for(int a=0; a< plugs.length; a++){ output.append(a + 1).append(" - ").append(plugs[a]).append(" | "); }
        output.append("Please Select a plugID (INTEGER ONLY)");
        return  output.toString();
    }

    public  double locationConverter(int roomNumber, int device){
        String roomNumberString = String.valueOf(roomNumber);
        String deviceString = String.valueOf(device);
        double plugLocation = Double.parseDouble(roomNumberString + "."+"0"+deviceString);
        return plugLocation;
    }

    // ----------------------------------------------------------------------\\

    //---------------------------- ROOM FUNCTIONS -----------------------------\\
    public String roomNamer(int roomNumber) {
        String stringRoomName = "";
        int n = 0;
        for(int i=0;i<rooms.length;i++){
            n = roomNumber;
            stringRoomName = rooms[n-1];}
        return stringRoomName;
    }


    public String roomList() {
        StringBuilder output = new StringBuilder();
        output.append("ROOMS AVAILABLE:\n");

        for (int a = 0; a < rooms.length; a++) { output.append(a + 1).append(" -  ").append(rooms[a]).append(" | "); }
        return output.toString();
    }

    // ----------------------------------------------------------------

    //------------------------------ DEVICE OPTIONS ---------------------- \\
    public String displayDeviceList(){
        StringBuilder output = new StringBuilder();
        output.append("AVAILABLE DEVICE LIST OPTIONS\n");
        output.append("These are the standard devices that can be attached to the Smart Plug:\n");
        for (int a = 0; a <deviceNames.length; a++) {
            output.append(a + 1).append(" -  ").append(deviceNames[a]).append(" | "); }
        return output.toString();
    }

    //--------------------------------------------------------------------------\\

    //--------------------------------- DISPLAYING DASHBOARD-----------------------\\
    public String Display(){
        StringBuilder output = new StringBuilder();
        output.append("                   -----------------DASHBOARD-----------------                    \n");
        Sort();
        for (int i = 0; i < rooms.length; i++) {
            output.append("ROOM:").append(i + 1).append("\n");

            for (SmartPlug plug : plugs) {
                String location = String.valueOf(plug.getLocation());
                String splitLocation = String.valueOf(location.split("\\.")[0]);

                if (Integer.parseInt(splitLocation) -1 == i){ output.append(plug.toString()); }
            }
        }
        output.append("----------------------------------------------------------------------- \n");
        return output.toString();
    }

    //-------------------------------------------------------------------------------------------\\

    //---------------------------------------SORTING LOCATIONS TO APPEAR IN DASHBOARD ---------------- \\
    public void Sort(){
        boolean  hasOrderChanged = true;
        while(hasOrderChanged){
            hasOrderChanged = false;
            for(int i = 1; i < plugs.length; i++){
                double plugA = plugs[i].getLocation();
                String plugADeviceName =plugs[i].getDeviceName();
                String stringPlugALocation = plugs[i].getRoomLocation();

                double plugB = plugs[i -1 ].getLocation();
                String plugBDeviceName = plugs[i-1].getDeviceName();
                String stringPlugBLocation = plugs[i-1].getRoomLocation();

                if(plugA < plugB){
                    plugs[i- 1].setLocation(plugA);
                    plugs[i-1].setDeviceName(plugADeviceName);
                    plugs[i-1].setRoomLocation(stringPlugALocation);

                    plugs[i].setLocation(plugB);
                    plugs[i].setDeviceName(plugBDeviceName);
                    plugs[i].setRoomLocation(stringPlugBLocation);

                    hasOrderChanged = true;
                }
            }
        }
    }

    //----------------------------------------------------------------------------\\

    //---------------------------------- HOUSE LEVEL OPTIONS----------------------------------\\

    public void houseToggle(int decision){
        switch (decision) {
            case 1 -> { for (SmartPlug object : plugs) { object.setStatus(false); } }
            case 2 -> { for (SmartPlug object : plugs) { object.setStatus(true); } }
        }
    }

    //----------------------------------------------------------------------------------------\\

    //-------------------------------- ROOM LEVEL OPTIONS --------------------------------------- \\
    public String roomChoiceOptions() {
        StringBuilder output = new StringBuilder();
        output.append("1 - Switch all Plugs Off\n 2- Switch all plugs On \n 3- Select a Plug");
        return output.toString();
    }

    public void roomOptions(int room_choice,int room_plug_option) {
        String room_number = String.valueOf(room_choice);
        int[] indexes = new int[plugs.length];
        int rooms_index = 0;

        for (int i = 0; i < plugs.length; i++) {
            SmartPlug object = plugs[i];
            String location = String.valueOf(object.getLocation());
            String splitLocation = location.split("\\.")[0];
            if (room_number.equals(splitLocation)) {
                indexes[rooms_index++] = i;

                switch (room_plug_option) {
                    case 1 -> {
                        //or (int i = 0; i < rooms_index; i++) {
                        //SmartPlug object = plugs[i];
                        object.setStatus(false);
                    }

                    case 2 -> {
                        //for (int i = 0; i < rooms_index; i++) {
                        //SmartPlug object = plugs[i];
                        object.setStatus(true);
                    }
                }
            }
        }
    }




    public String roomOptionsChoice3List(int room_choice, int room_plug_option){
        String stringRoomNumber = String.valueOf(room_choice);
        StringBuilder output = new StringBuilder();
        int[] indexes = new int[plugs.length];
        int roomsIndex = 0;
        for (int i = 0; i < plugs.length; i++) {
            SmartPlug object = plugs[i];
            String stringLocation = String.valueOf(object.getLocation());
            String SplitRoomLocation = stringLocation.split("\\.")[0];
            if (stringRoomNumber.equals(SplitRoomLocation)) {
                indexes[roomsIndex++] = i;
                output.append(stringLocation).append("\n");
            }
        }return output.toString();
    }

    public String roomOptionsChoice3(int roomChoice, int room_plug_option, int device) {
        String roomNumber = String.valueOf(roomChoice);
        StringBuilder output = new StringBuilder();
        int[] indexes = new int[plugs.length];
        int rooms_index = 0;
        for (int i = 0; i < plugs.length; i++) {
            SmartPlug object = plugs[i];
            String stringLocation = String.valueOf(object.getLocation());
            String stringRoomLocation = stringLocation.split("\\.")[0];
            if (roomNumber.equals(stringRoomLocation)) { indexes[rooms_index++] = i; }
        }

        for (int i = 0; i < rooms_index; i++) {
            SmartPlug object = plugs[i];
            String location = String.valueOf(object.getLocation());
        }
        plugToggle(roomNumber, device);
        output.append("PLUG TOGGLED");
        return output.toString();
    }
    //------------------------------------------------------------------------------------------\\

//-------------------------------------------------- PLUG DEVICE OPTIONS -----------------\\

    public String plugOptions(int plugChoice){
        StringBuilder output = new StringBuilder();
        String roomNumber = String.valueOf(plugChoice);
        output.append("1 - Switch Plug Off | 2- Switch Plug On | 3 - Change Attached Device | 4 - Move Plug to a different room\n");
        return output.toString();
    }
    public void plugToggle(String roomNumber, int device) {
        String stringRoomNumber = String.valueOf(roomNumber);
        String stringValueDevice = String.valueOf(device);
        String stringDevice = "0" + stringValueDevice;

        for (SmartPlug object : plugs) {
            String stringLocation = String.valueOf(object.getLocation());
            String stringRoomLocation = stringLocation.split("\\.")[0];
            String stringDeviceLocation = stringLocation.split("\\.")[1];

            if (stringRoomLocation.equals(stringRoomNumber)) {
                if (stringDevice.equals(stringDeviceLocation)) {
                    object.toggle();
                }
            }
        }
    }

    public void plugDeviceOptions(int plugChoice, int plugOnOff) {
        int plugID = plugChoice;
        for (SmartPlug object : plugs) {
            int location = (object.getID());

            if (plugID == (location)) {
                switch (plugOnOff) {
                    case 1: { object.setStatus(false); }
                    break;
                    case 2: { object.setStatus(true); }
                    break;
                }
            }
        }
    }

    public String plugDeviceOptionsChoice3(int plugChoice, int plugOnOff) {
        StringBuilder output = new StringBuilder();
        int plugID = plugChoice;
        for (SmartPlug object : plugs) {
            int location = (object.getID());

            if (plugID == (location)) {
                output.append("AVAILABLE DEVICE LIST OPTIONS\n");
                for (int a = 0; a <deviceNames.length; a++) {
                    output.append(a + 1).append(" -  ").append(deviceNames[a]).append(" | "); }
            }
        }return output.toString();
    }

    public void plugOptionsChangeDevice(int plugChoice, int plugOnOff, int plugDevice) {

        int plugID = plugChoice;
        for (SmartPlug object : plugs) {
            int location = (object.getID());
            if (plugID == (location)) {
                int device = plugDevice;
                object.changeAttachedDevice(device, deviceNames[plugDevice-1]);
            }
        }
    }

    public String plugDeviceChangeLocation(int plugChoice, int plugOnOff) {
        StringBuilder output = new StringBuilder();
        output.append("ROOMS AVAILABLE:\n");
        for (int a = 0; a < rooms.length; a++) { output.append(a + 1).append(" -  ").append(rooms[a]).append(" | "); }
        output.append("PLEASE SELECT A ROOM (integer ONLY) ");
        return output.toString();
    }

    public void plugDeviceChoice4RoomLocation(int plugChoice, int plugOnOff, int newRoom) {
        for (SmartPlug object : plugs) {
            int location = (object.getID());
            int plugID = plugChoice;

            if (plugID == location) {
                String roomlocation = String.valueOf(object.getLocation());
                String splitLocation = roomlocation.split("\\.")[1];
                String newLocation = (newRoom + splitLocation);
                double updatedLocation = Double.parseDouble(newLocation);
                object.change_Location(newRoom);
                object.setRoomLocation(String.valueOf(rooms[newRoom - 1]));
            }
        }
    }

    //-----------------------------------------------------------------------------------------------------------------------\\

    //------------------------------- SYSTEM LEVEL OPTIONS -----------------------------------\\
    public String system_list(){
        StringBuilder output = new StringBuilder();
        output.append("SYSTEM OPTIONS AVAILABLE:\n");
        output.append("1 - ADD SMART PLUGS | 2 - ADD DEVICES | 3 - ADD ROOMS");
        return  output.toString();
    }
    //---------------------------------------------------------------------------\\
}
