use std::collections::VecDeque;
// use regex::Regex;
use fancy_regex::Regex;

#[derive(Debug)]
struct Note {
    contents: String,
    hidden: bool,
}

#[derive(Debug)]
pub struct User {
    username: String,
    password: String,
    notes: Vec<Note>,
    max_notes: usize,
}

impl User {
    pub fn new(username: String, password: String) -> Self {
        Self {
            username,
            password,
            notes: Vec::new(),
            max_notes: 0,
        }
    }

    pub fn set_max_notes(&mut self, max_notes: usize) {
        self.max_notes = max_notes;
    }

    pub fn check_credentials(&self, test_username: &str, test_password: &str) -> bool {
        self.username == test_username && self.password == test_password
    }

    pub fn add_note(&mut self, contents: String, hidden: bool) -> Result<(), String> {
        if self.notes.len() == self.max_notes {
            return Err("Notes capacity reached".into());
        }
        self.notes.push(Note { contents, hidden });
        Ok(())
    }

    pub fn get_note(&self, idx: usize) -> Option<String> {
        if idx < self.notes.len() && !self.notes[idx].hidden {
            Some(self.notes[idx].contents.clone())
        } else {
            None
        }
    }

    pub fn find_note(&self, contains: &str) -> Vec<usize> {
        let re = Regex::new(format!("^.*{contains}.*$").as_str()).unwrap();
        self.notes
            .iter()
            .enumerate()
            .filter_map(|(i, note)| {
                let re_match = re.captures(&note.contents);
                (re_match.is_ok() && re_match.ok().is_some() && !note.hidden).then_some(i)
            })
            .collect()
    }
}

pub struct UserManager {
    permanent_users: Vec<User>,
    users: VecDeque<User>,
    user_capacity: usize,
    max_notes_per_user: usize,
    max_note_length: usize,
}

impl UserManager {
    pub fn new(user_capacity: usize, max_notes_per_user: usize, max_note_length: usize) -> Self {
        Self {
            permanent_users: Vec::new(),
            users: VecDeque::new(),
            user_capacity,
            max_notes_per_user,
            max_note_length,
        }
    }

    pub fn debug(&self) -> String {
        format!("{:?}", self.users)
    }

    pub fn add_permanent_user(&mut self, user: User) {
        self.permanent_users.push(user);
    }

    pub fn add_user(&mut self, username: &str, password: &str) -> Result<(), String> {
        if self
            .users
            .iter()
            .chain(self.permanent_users.iter())
            .any(|existing_user| existing_user.username == username)
        {
            return Err("User already exists".into());
        }

        let mut user = User::new(username.to_owned(), password.to_owned());
        if self.user_capacity > 0 {
            if self.users.len() >= self.user_capacity {
                self.users.pop_front();
            }
            user.set_max_notes(self.max_notes_per_user);
            self.users.push_back(user);
        }
        Ok(())
    }

    pub fn add_note_for_user(&mut self, username: &str, contents: &str) -> Result<usize, String> {
        let user = self
            .users
            .iter_mut()
            .chain(self.permanent_users.iter_mut())
            .find(|user| user.username == username)
            .ok_or("Invalid user")?;
        user.add_note(
            contents[..std::cmp::min(contents.len(), self.max_note_length)].to_owned(),
            false,
        )?;
        Ok(user.notes.len() - 1)
    }

    pub fn get_note_for_user(&self, username: &str, idx: usize) -> Result<String, String> {
        Ok(self
            .users
            .iter()
            .chain(self.permanent_users.iter())
            .find(|user| user.username == username)
            .ok_or("Invalid user")?
            .get_note(idx)
            .ok_or("No such note")?)
    }

    pub fn find_note_for_user(&self, username: &str, contains: &str) -> Result<Vec<usize>, String> {
        Ok(self
            .users
            .iter()
            .chain(self.permanent_users.iter())
            .find(|user| user.username == username)
            .ok_or("Invalid user")?
            .find_note(contains))
    }

    pub fn find_user(&self, username: &str, password: &str) -> bool {
        self.users
            .iter()
            .chain(self.permanent_users.iter())
            .any(|user| user.check_credentials(username, password))
    }
}
