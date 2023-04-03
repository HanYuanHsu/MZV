#include <iostream>
#include <string>
#include <map>

using namespace std;

struct Node { //no *
    string heading;
    int coefficient;
    bool ended = false;
    Node *left, *right;

    Node() {heading="", coefficient=0;}
	Node(string h, int c) {heading = h, coefficient = c;} //, or ;
};

// Node* External = new Node("", 0);

Node* Build(string u, string v, string h) { // u shuffle v; h: heading
    if (u == "") {
        Node* n = new Node();
        n->heading = h + v;
        n->ended = true;
        return n;
    }
    else if (v == "") {
        Node* n = new Node();
        n->heading = h + u;
        n->ended = true;
        return n;
    }

    Node* n = new Node();
    n->heading = h;


    string x = ""; x += u.at(0);
    string u_no_x; u_no_x.assign(u, 1, u.length()-1);
    string hx = h + x;
    n->left = Build(u_no_x, v, hx);

    string y = ""; y += v.at(0);
    string v_no_y; v_no_y.assign(v, 1, v.length()-1);
    string hy = h + y;
    n->right = Build(u, v_no_y, hy);

    return n;
}

void traverse(Node* n, map<string, int> m) {
    if (n->ended) {
        string h = n->heading;
        if (m.find(h) == m.end()) { // key for h not created yet
            m[h] = 1;
        }
        else {
            m[h]++;
        }
        return ;
    }
    traverse(n->left, m);
    traverse(n->right, m);
}

void pre_traverse(Node *n) {
    if (n->ended) return;

    cout << n->heading << " ";
    pre_traverse(n->left);
    pre_traverse(n->right);
}

int main()
{
    /*
    string s = "1234";
    string t;
    t = t.assign(s, 1, s.length()-1);
    string u = "";
    u += s[0];
    cout << s << t << u << endl;
    */

    Node* N = Build("10", "100", "");
    map<string, int> m;
    pre_traverse(N);

    return 0;
}

