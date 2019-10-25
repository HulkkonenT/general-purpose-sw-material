//============================================================================
// Name        : Pytha.cpp
// Author      : thu
// Version     : 1.0
// Copyright   : Thu
// Description : Program inputs the given triangle legs as inches, converts
//               them to metres, and finally calculates hypotenusas according
//               to Pythagoras statement.
//============================================================================

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

struct triangle_info_t {
    double leg_a;
    double leg_b;
    double hypotenusa;
};

// compare sequential hypotenusas
bool cmp_hypo(triangle_info_t inf1, triangle_info_t inf2) {
        return (inf1.hypotenusa < inf2.hypotenusa);
     };

int main(int argc, char* argv[]) {

    triangle_info_t tri_info;
    string line;
    size_t sz = 0;

    vector<triangle_info_t> v;

    ifstream input_file;
    ofstream output_file;

    const int arg_cnt = 3;

    if (argc != 3) {
        cerr << "incorrect argument count: " << argc << ", should be: " << arg_cnt << endl;
        return -1;
    }

    input_file.open(argv[1], ios::in); //open the given input leg data file in read mode
    if (input_file.is_open()) {
        output_file.open(argv[2], ios::out); //open the given output leg data file in write mode
        if (output_file.is_open()) {
            while (getline(input_file,line)) {
                if (line[0]>='0' && line[0]<='9') {
                    tri_info.leg_a = stod(line,&sz) * 0.3048; //string to decimal and unit foot to unit meter conversion
                    tri_info.leg_b = stod(line.substr(sz)) * 0.3048;
                    tri_info.hypotenusa = sqrt(pow(tri_info.leg_a,2) + pow(tri_info.leg_b,2));
                    v.push_back(tri_info); //push into vector
                }
            }
            sort(v.begin(), v.end(), cmp_hypo); //sort according to hypotenusa
            output_file << "legA" << setw(8) << "legB" << setw(16) << "hypotenusa" << endl;
            for (auto x : v) {
                output_file << setw(0) << x.leg_a << setw(8) << x.leg_b << "   " <<  x.hypotenusa << "\n";
            }
            output_file.close();
        }
        else cout << "unable to open output_file" << endl;
        input_file.close();
    }
    else cout << "unable to open input_file" << endl;

	return 0;
}
