#![allow(non_snake_case)]


use std::io::BufReader;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let input = File::open("input").expect("File not opening");
    let input_reader = BufReader::new(input);
    let mut calories: Vec<i32> = Vec::new();
    let mut sum: i32 = 0;
    // println!("{:?}", input_reader);
    for line_result in input_reader.lines() {
        let mut line = line_result.expect("Couldn't read line from 'input_reader'");
        line = line.trim().to_string();
        if line == "" { 
            calories.push(sum);
            sum = 0;a
            // println!("New Elf"); 
        } else {
            // println!("{}", line);
            sum = sum
                + line
                    .parse::<i32>()
                    .expect("Error while parsing calories to i32");
        } 
    }
    calories.push(sum);
    // Part1
    calories.sort();
    calories.reverse();
    println!("Most calories: {:?}", calories.first().unwrap());
    
    // Part 2
    sum = 0;
        for i in 0..3 {
        sum = sum + calories[i];
    }
    println!("Sum of calories: {:?}", sum);
}

