// read txt file

fn read_file(path_to_file: &str) -> Result<String, std::io::Error> {
    std::fs::read_to_string(path_to_file)
}

fn main() {
    let path_to_file = "input.txt";
    let input: String = match read_file(path_to_file) {
        Ok(str) => str,
        Err(error) => panic!("Problem opening the file: {:?}", error),
    };
    println!("{input}");
}
