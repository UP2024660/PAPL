package Coursework;

public class SmartPlug {
    private String deviceName;
    private boolean plugStatus;
    private double plugLocation;
    private int plugID;
    private String Room;


    public SmartPlug(Boolean plugStatus, double plugLocation, int plugID, String deviceName, String RoomName){
        this.plugLocation = plugLocation; this.plugStatus = plugStatus; this.plugID = plugID;
        this.deviceName = deviceName; this.Room = RoomName;
    }

    public boolean isStatus(){ return plugStatus; }

    public void setStatus(boolean status){ this.plugStatus = status; }

    public void toggle(){ setStatus(!isStatus()); }

    public double getLocation(){return this.plugLocation;}
    public String getRoomLocation(){return this.Room;}

    public String getDeviceName(){return this.deviceName;}
    public void setDeviceName(String deviceName){this.deviceName = deviceName;}

    public int getID(){return this.plugID;}

    public void setLocation(double location){ this.plugLocation = location; }
    public void setRoomLocation(String room_location){this.Room = room_location;}

    public void changeAttachedDevice(int DeviceNumber, String DeviceName){ //change attached device
        String stringFullLocation = String.valueOf(getLocation());
        String stringSplitRoomLocation = stringFullLocation.split("\\.")[0];
        String stringDeviceNumber = (".0"+(DeviceNumber));
        String stringNewDevice = (stringSplitRoomLocation+stringDeviceNumber);
        double doubleNewDevice = Double.parseDouble(stringNewDevice);
        String newDeviceName = DeviceName;
        this.deviceName = newDeviceName;
        this.plugLocation = doubleNewDevice; }

    public void change_Location(int newRoomNumber){  ///change device Location
        String stringFullLocation = String.valueOf(getLocation());
        String stringSplitDeviceLocation = stringFullLocation.split("\\.")[1];
        String stringNewRoomNumber = String.valueOf(newRoomNumber);
        String stringDeviceNumber = (stringNewRoomNumber+"."+stringSplitDeviceLocation);
        double doubleNewLocation = Double.parseDouble(stringDeviceNumber);
        this.plugLocation = doubleNewLocation; }

    @Override
    public String toString(){
        return
                "SmartPlug | Attached to:"+ deviceName+" "+
                        plugLocation+
                        "                             | Room: " + Room +
                        "| ID: " + plugID +
                        "  |status: " + plugStatus + "|"+
                        "\n"; }
}
