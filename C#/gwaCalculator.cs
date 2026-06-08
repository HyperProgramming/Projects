using System;

/*
    GWA Calculator in C#
    Program asks for 4 courses, grades and units
    After that, it calculates and shows you your GWA
*/

class Program
{
    static void Main()
    {
        Console.Write("Enter your name: ");
        string studName = Console.ReadLine();
        Console.Write("Enter your section: ");
        string studSec = Console.ReadLine();

        Console.Write("\nEnter course code 1: ");
        string cCode1 = Console.ReadLine();
        Console.Write("Enter course grade 1: ");
        if (!float.TryParse(Console.ReadLine(), out float cGrade1)) // simple error handling if user input are not numerals
        {
            Console.Write("Error: Invalid Input");
            Environment.Exit(1);
        }
        Console.Write("Enter course unit 1: ");
        if (!int.TryParse(Console.ReadLine(), out int cUnit1))
        {
            Console.Write("Error: Invalid Input");
            Environment.Exit(1);
        }

        
        Console.Write("\nEnter course code 2: ");
        string cCode2 = Console.ReadLine();
        Console.Write("Enter course grade 2: ");
        if (!float.TryParse(Console.ReadLine(), out float cGrade2)) 
        {
            Console.Write("Error: Invalid Input");
            Environment.Exit(1);
        }
        Console.Write("Enter course unit 2: ");
        if (!int.TryParse(Console.ReadLine(), out int cUnit2))
        {
            Console.Write("Error: Invalid Input");
            Environment.Exit(1);
        }

        
        Console.Write("\nEnter course code 3: ");
        string cCode3 = Console.ReadLine();
        Console.Write("Enter course grade 3: ");
        if (!float.TryParse(Console.ReadLine(), out float cGrade3)) 
        {
            Console.Write("Error: Invalid Input");
            Environment.Exit(1);
        }
        Console.Write("Enter course unit 3: ");
        if (!int.TryParse(Console.ReadLine(), out int cUnit3))
        {
            Console.Write("Error: Invalid Input");
            Environment.Exit(1);
        }

        
        Console.Write("\nEnter course code 4: ");
        string cCode4 = Console.ReadLine();
        Console.Write("Enter course grade 4: ");
        if (!float.TryParse(Console.ReadLine(), out float cGrade4)) 
        {
            Console.Write("Error: Invalid Input");
            Environment.Exit(1);
        }
        Console.Write("Enter course unit 4: ");
        if (!int.TryParse(Console.ReadLine(), out int cUnit4))
        {
            Console.Write("Error: Invalid Input");
            Environment.Exit(1);
        }

        Console.WriteLine("\nStudent Name:" + studName); 
        Console.WriteLine("Student Section:" + studSec);
        Console.WriteLine("\nCOURSES    UNITS    GRADE");
        Console.WriteLine($"{cCode1,-10} {cUnit1,-8} {cGrade1}"); // string interpolation to align their format
        Console.WriteLine($"{cCode2,-10} {cUnit2,-8} {cGrade2}"); // putting the $ will allow us to embed variables directly inside a string
        Console.WriteLine($"{cCode3,-10} {cUnit3,-8} {cGrade3}"); // putting -10 and -8 will give us 10 and 8 character wide space aligned to the left for proper display on output
        Console.WriteLine($"{cCode4,-10} {cUnit4,-8} {cGrade4}"); // cGrade doesn't need one since it's at the end

        
        int totUnits = cUnit1 + cUnit2 + cUnit3 + cUnit4; // gets total unit
        float gwa = ((cGrade1 * cUnit1) + (cGrade2 * cUnit2) + (cGrade3 * cUnit3) + (cGrade4 * cUnit4)) / totUnits; // calculates gwa

        Console.WriteLine($"\nGWA: {gwa:F2}"); // displays gwa, formatting to F2 so it only shows 2 decimals
    }
}
