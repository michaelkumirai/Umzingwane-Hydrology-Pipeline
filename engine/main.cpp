#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <cmath>
#include <string>
#include <sstream>  // <--- This is the one missing!
#include <numeric>
#include <algorithm>

int main(int argc, char* argv[]) {
    if (argc < 4) {
        std::cerr << "Usage: " << argv[0] << " <csv_file> <params_file> <num_simulations>" << std::endl;
        return 1;
    }

    // 1. Read Parameters from ML file
    std::ifstream pfile(argv[2]);
    double mean_param, vol_param;
    pfile >> mean_param >> vol_param;

    // 2. Read starting flow from CSV
    std::ifstream file(argv[1]);
    std::string line, val;
    double last_flow = 0.0;
    std::getline(file, line); // Skip Header
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::getline(ss, val, ','); std::getline(ss, val, ',');
        if (!val.empty()) last_flow = std::stod(val);
    }

    int num_sims = std::stoi(argv[3]);
    std::mt19937 gen(std::random_device{}());
    std::normal_distribution<double> dist(0.0, vol_param);

    std::vector<double> sim_results;
    
    // Pure Random Walk Simulation (No Memory)
    for (int s = 0; s < num_sims; ++s) {
        double current_val = last_flow;
        double max_peak = 0.0;
        
        for (int i = 0; i < 12; ++i) {
            current_val += dist(gen);
            if (current_val < 0) current_val = 0;
            if (current_val > max_peak) max_peak = current_val;
        }
        sim_results.push_back(max_peak);
    }

    std::sort(sim_results.begin(), sim_results.end());

    // Output FDC
    std::vector<double> probs = {0.01, 0.05, 0.1, 0.2, 0.5, 0.9, 0.99};
    std::cout << "Exceedance | Peak Discharge (m^3/s)" << std::endl;
    for (double p : probs) {
        int idx = (int)((1.0 - p) * (sim_results.size() - 1));
        double cms = (sim_results[idx] * 1000.0) / 2592000.0;
        std::cout << "Q" << (int)(p*100) << " \t   | " << cms << std::endl;
    }

    return 0;
}