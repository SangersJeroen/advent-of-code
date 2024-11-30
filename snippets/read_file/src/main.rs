// read txt file

fn read_file(path_to_file: &str) -> String {
    std::fs::read_to_string(path_to_file).expect("FileNotFoundError")
}

fn main() {
    let path_to_file = "input.txt";
    let input: String = read_file(path_to_file);
    println!("{}", input)
}
