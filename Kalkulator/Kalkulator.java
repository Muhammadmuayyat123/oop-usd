/* Muhammad muayyat sabir
 * D0221114
 * Informatika H
 */

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package maiin;

/**
 *
 * @author yayat
 */
public class Kalkulator {
    double nilai1;
    double nilai2;
    
    void isiNilai1(double x){
        nilai1 = x;
    }
    
    void isiNilai2(double y){
        nilai2 = y;
    }
    
    double tambah(){
        return nilai1 + nilai2;
    }
    
    double kurang(){
        return nilai1 - nilai2;
    }
    
    double kali(){
        return nilai1 * nilai2;
    }
    
    double bagi(){
        return nilai1 / nilai2;
    }
    
    void Eksekusi(){
    System.out.println("Perjumlahan : " + tambah());
    System.out.println("Pengurangan : " + kurang());
    System.out.println("Perkalian : " + kali());
    System.out.println("Pembagian : " + bagi());
}
}
