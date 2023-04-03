#include <iostream>
#include <string>
#include <sstream>
#include <queue>
#include <map>

using namespace std;

map<string, int> m;

string convert(int n) {
stringstream ss;
string output;
ss << n;
ss >> output;
return output;
}
int toInt(string s) {
stringstream ss;
int output;
ss << s;
ss >> output;
return output;
}

void stuffle(string head, queue<int> s, queue<int> t) {
if (s.empty()) {
    while (!t.empty()) {
        head = head + " " + convert(t.front());
        t.pop();
    }
    map<string, int>::iterator it = m.find(head);
    if (it == m.end()) {
         m[head] = 1;
    }
    else {
        it->second++;
    }
    return;
}
if (t.empty()) {
    while (!s.empty()) {
        head = head + " " + convert(s.front());
        s.pop();
    }
    map<string, int>::iterator it = m.find(head);
    if (it == m.end()) {
         m[head] = 1;
    }
    else {
        it->second++;
    }
    return;
}

string heads = head + " " + convert(s.front());
string headt = head + " " + convert(t.front());
string headspt = head + " " + convert(s.front() + t.front());
queue<int> s0 = s;
s.pop();
stuffle(heads, s, t); 
t.pop();
stuffle(headt, s0, t); // s0 has not changed
stuffle(headspt, s, t); // both s, t have changed
}

int main()
{
    string str1, str2, str;
    while (getline(cin, str1) && getline(cin, str2)) {
        queue<int> s, t;

        stringstream ss_1;
        ss_1 << str1;
        while (ss_1 >> str) {
            s.push(toInt(str));
        }
        stringstream ss_2;
        ss_2 << str2;
        while (ss_2 >> str) {
            t.push(toInt(str));
        }

        stuffle("", s, t);
        for (map<string, int>::iterator it = m.begin(); it != m.end(); it++) {
            cout << it->first << ": " << it->second << endl;
        }
        m.clear();
    }
    return 0;
}
