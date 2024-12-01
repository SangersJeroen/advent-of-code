use std::env;

fn main() {
    // Read file path from command line
    let args: Vec<String> = env::args().collect();
    let file = &args[1];
    // Part 1
    // Read file into list of ints where each line is an int
    let input = fs::read_to_string(file).unwrap();
    let input: Vec<i32> = input.lines().map(|x| x.parse::<i32>().unwrap()).collect();
}
