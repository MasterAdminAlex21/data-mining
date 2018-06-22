package proyecto;

import java.awt.*;
import javax.swing.*;
import java.lang.*;

public class vista1 extends JFrame{
 private JLabel ex;
 private JButton boton;

 public vista1(){
  setTitle("Ejemplo de vista");
  setSize(800,500);
  setVisible(true);
  setResizable(true);
  setDefaultCloseOperation(EXIT_ON_CLOSE);
  setLocation(100,100);

  Font pers=new Font("Arial",Font.ITALIC,24);

  ex=new JLabel("Ejemplo DE PUTO LABEL CARAJO ALV >:V");
  ex.setFont(pers);
  ex.setForeground(Color.getHSBColor(50,100,20));
  ex.setSize(200,50);

  boton=new JButton("Pinshi boton de panico alv");
  boton.setSize(200,50);

  Container pane=getContentPane();
  pane.setLayout(new GroupLayout(pane));

  pane.add(ex).setLocation(100,100);

  pane.add(boton).setLocation(300,50);
 }

 public static void main(String [] args){
  new vista1().setVisible(true);
 }
}