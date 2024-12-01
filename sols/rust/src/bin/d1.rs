use std::iter::zip;

pub fn part_one(llist: &Vec<i32>, rlist: &Vec<i32>) -> i32 {
    zip(llist, rlist)
        .map(|(ll, rr)| (ll - rr).abs())
        .sum::<i32>()
}

pub fn part_two(llist: &Vec<i32>, rlist: &Vec<i32>) -> i32 {
    let mut counts: Vec<i32> = Vec::new();
    for ll in llist {
        let mut count: i32 = 0;
        for rr in rlist {
            if ll == rr {
                count += 1
            }
        }
        counts.push(count);
    }
    zip(llist, counts).map(|(ll, cc)| (ll * cc)).sum::<i32>()
}

pub fn main() {
    let input =
        std::fs::read_to_string("/home/jeroensangers/Repos/advent_of_code/inputs/d1_p1.txt")
            .unwrap();
    let mut llist: Vec<i32> = Vec::new();
    let mut rlist: Vec<i32> = Vec::new();
    input
        .split("\n")
        .filter(|s| !s.is_empty())
        .map(|s| {
            let mut splits = s.split_whitespace();
            (
                splits.next().unwrap().parse::<i32>().unwrap(),
                splits.next().unwrap().parse::<i32>().unwrap(),
            )
        })
        .for_each(|(l, r)| {
            llist.push(l);
            rlist.push(r);
        });
    llist.sort();
    rlist.sort();

    println!("part one answer {}", part_one(&llist, &rlist));
    println!("part two answer {}", part_two(&llist, &rlist));
}
