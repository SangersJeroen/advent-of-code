// read txt file

fn read_file(path_to_file: &str) -> str {
    let input = std::fs::read_to_string(path_to_file).expect("Unable to read file");
    input
}

fn main() {
    let path_to_file = "input.txt";
    let input = read_file(path_to_file);
    println!("{}", input)
}
