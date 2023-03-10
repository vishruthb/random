#include <bits/stdc++.h>
using namespace std;

// Macros
#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define vi vector<int>
#define vpi vector<pair<int, int>>
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define rev(i, a, b) for (int i = (a); i >= (b); --i)
#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()
#define endl "\n"

// Constants
const int INF = 0x3f3f3f3f;
const ll LL_INF = 0x3f3f3f3f3f3f3f3f;

// Utility functions
template<typename T> void ckmin(T& a, T b) { a = min(a, b); }
template<typename T> void ckmax(T& a, T b) { a = max(a, b); }
template<typename T> bool ckmin_bool(T& a, T b) { if (a > b) { a = b; return true; } return false; }
template<typename T> bool ckmax_bool(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<typename T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
template<typename T> T lcm(T a, T b) { return a * (b / gcd(a, b)); }
template<typename T> bool is_prime(T n) { if (n < 2) return false; for (T i = 2; i * i <= n; i++) if (n % i == 0) return false; return true; }

// Debugging functions
template<typename T> void debug(T a) { cerr << a << endl; }
template<typename T1, typename... T2> void debug(T1 a, T2... b) { cerr << a << " "; debug(b...); }

// Main function
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // TODO: Solve the problem

    return 0;
}
