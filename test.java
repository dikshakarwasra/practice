class Test{
    int roll;
    String name;
    void insert(int r, String n){
        roll = r;
        name = n;
    }
    void show(){
        System.out.println(roll+" "+name);
    }
    public static void main(String args[]){
        Test t = new Test();
        t.insert(15,"Diksha karwasra ji");
        t.show();
    }
}
