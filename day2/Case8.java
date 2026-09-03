class Case8{
    public static void main(String [] args) {
   Case8 obj = new Case8();
     int a = obj.sum(5);
     System.out.println(a);
    }
    int sum(int b){
        if(b>0){
            return b + sum(b-1);
        }
        else{
            return 0;
        }
     }
  
}
