/* Niekde tam je zrejme este nejaka chyba, mozno nerusenie pocitadla dvojak pri dostani sa do JAIL z ineho dovodu ako 3 dvojky */
#include <iostream>
#include <sstream>
#include <math.h>
using namespace std;

string Box[] =
{
    "GO",
    "A1",
    "CC1",
    "A2",
    "T1",
    "R1",
    "B1",
    "CH1",
    "B2",
    "B3",
    "JAIL",
    "C1",
    "U1",
    "C2",
    "C3",
    "R2",
    "D1",
    "CC2",
    "D2",
    "D3",
    "FP",
    "E1",
    "CH",
    "E2",
    "E3",
    "R3",
    "F1",
    "F2",
    "U2",
    "F3",
    "G2J",
    "G1",
    "G2",
    "CC3",
    "G3",
    "R4",
    "CH3",
    "H1",
    "T2",
    "H2"
};

double D6[] = { 1.0 / 36, 2.0 / 36, 3.0 / 36, 4.0 / 36, 5.0 / 36, 6.0 / 36, 5.0 / 36, 4.0 / 36, 3.0 / 36, 2.0 / 36, 1.0 / 36 };
double D4[] = { 1.0 / 16, 2.0 / 16, 3.0 / 16, 4.0 / 16, 3.0 / 16, 2.0 / 16, 1.0 / 16 };
double B_final[40];
double *B_all[4];
double B_not_two[40];

void play(int dice, bool twos, double twos_temp[4][40] = nullptr, int index = 0);
void process_turn(int target_box, double landing_chance, double * dest);

int main(int argc, char** argv)
{
    if (argc < 3)
    {
        cout << "Enter dice sides and turns count" << endl;
        return 0;
    }

    int dice;
    int turns;

    istringstream ssd(argv[1]);
    if (!(ssd >> dice))
    {
        cout << "Non-integer dice sides" << endl;
        return 0;
    }

    istringstream ssr(argv[2]);
    if (!(ssr >> turns))
    {
        cout << "Non-integer turns count" << endl;
        return 0;
    }

    for (int i = 0; i < 4; i++)
    {
        B_all[i] = new double[40];
    }

    B_not_two[0] = 1.0;
    copy(B_not_two, B_not_two + 40, B_all[0]);
    for (int t = 0; t < turns; t++)
    {
        double B_two_temp[3][40];
        for (int i = 1; i < 3; i++)
            fill(B_two_temp[i], B_two_temp[i] + 40, 0.0);

        copy(B_not_two, B_not_two + 40, B_two_temp[0]);
        for (int t_c = 0; t_c < 2; t_c++)
        {
            play(dice, true, B_two_temp, t_c);
        }

        for (int i = 1; i < 3; i++)
        {
            for (int j = 0; j < 40; j++)
            {
                B_all[i][j] += B_two_temp[i][j];
            }
        }

        fill(B_not_two, B_not_two + 40, 0.0);
        play(dice, false);
        if (t > 1)
            B_not_two[10] += pow((dice == 4 ? D4[0] : D6[0]), 3);
        for (int j = 0; j < 40; j++)
        {
            B_all[1][j] += B_not_two[j];
        }
        fill(B_all[0], B_all[0] + 40, 0.0);
        double * temp = B_all[0];
        for (int i = 1; i < 4; i++)
        {
            B_all[i - 1] = B_all[i];
        }
        B_all[3] = temp;
        for (int j = 0; j < 40; j++)
        {
            B_final[j] += B_all[0][j];
        }
    }
    
    for (int i = 0; i < 4; i++)
    {
        delete[] B_all[i];
    }



    for (int i = 0; i < 40; i++)
    {
        cout << Box[i] << "(" << i << ")" << ": " << B_final[i] / turns << endl;
    }
}

void play(int dice, bool twos, double twos_temp[4][40], int index)
{
    double * source;
    double * destination;
    if (!twos)
    {
        source = B_all[0];
        destination = B_not_two;
    }
    else
    {
        source = twos_temp[index];
        destination = twos_temp[index + 1];
    }

    for (int b = 0; b < 40; b++)
    {
        if (source[b] > 0)
        {
            if (twos)
            {
                if (index == 2)
                {
                    destination[10] += source[b] * (dice == 4 ? D4[0] : D6[0]);
                }
                else
                {
                    int target = (b + 2) % 40;
                    process_turn(target, source[b] * (dice == 4 ? D4[0] : D6[0]), destination);
                }

            }
            else
            {
                for (int s = 1; s < (dice == 4 ? 7 : 11); s++)
                {
                    int target = (b + 2 + s) % 40;
                    process_turn(target, source[b] * (dice == 4 ? D4[s] : D6[s]), destination);
                }
            }
        }
    }
}

void process_turn(int target_box, double landing_chance, double * dest)
{
    if (target_box == 30)               // G2J
    {
        dest[10] += landing_chance;
        return;
    }


    if (target_box == 2 || target_box == 17 || target_box == 33)
    {
        dest[0] += 1.0 / 16 * landing_chance;       // Advance to GO
        dest[10] += 1.0 / 16 * landing_chance;      // G2J
        dest[target_box] += 14.0 / 16 * landing_chance;
        return;
    }

    if (target_box == 7 || target_box == 22 || target_box == 36)
    {
        dest[0] += 1.0 / 16 * landing_chance;       // Advance to GO
        dest[10] += 1.0 / 16 * landing_chance;      // G2J
        dest[11] += 1.0 / 16 * landing_chance;       // C1
        dest[24] += 1.0 / 16 * landing_chance;      // E3
        dest[39] += 1.0 / 16 * landing_chance;       // H2
        dest[5] += 1.0 / 16 * landing_chance;      // R1

        if (target_box == 7)
        {
            dest[15] += 2.0 / 16 * landing_chance;       // R2
            dest[12] += 1.0 / 16 * landing_chance;      // U1
        }

        else if (target_box == 22)
        {
            dest[25] += 2.0 / 16 * landing_chance;       // R3
            dest[28] += 1.0 / 16 * landing_chance;      // U2
        }

        else
        {
            dest[5] += 2.0 / 16 * landing_chance;       // R1
            dest[12] += 1.0 / 16 * landing_chance;      // U1
        }

        if (target_box == 36)
        {
            process_turn(target_box - 3, 1.0 / 16 * landing_chance, dest);
        }
        else
        {
            dest[target_box - 3] += 1.0 / 16 * landing_chance;
        }

        dest[target_box] += 6.0 / 16 * landing_chance;
        return;
    }

    dest[target_box] += landing_chance;
}
