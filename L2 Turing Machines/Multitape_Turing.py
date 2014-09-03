from __future__ import print_function
from itertools import izip

class TuringMachine(object):

    BINARY = set("01b")
    DIRECTION = set("RLS")

    def __init__(self, num_states, transitions, 
                 start=0, accept=1, reject=2, alphabet=BINARY):
        """Initialize machine, and validate.
        """

        self.num_states  = num_states
        self.transitions = transitions
        self.start       = start
        self.accept      = accept
        self.reject      = reject
        self.alphabet    = alphabet
        
        # split the transition dictionary for validation
        x_dom, x_rng = zip(*transitions.iteritems())

        # verfiy transition domain and range are uniformly sized
        size1 = self.size(x_dom)
        size2 = self.size(x_rng)

        # number of tapes is implicitly specified
        self.num_tapes = size1 - 1

        # verify that their sizes match
        assert size1 + self.num_tapes == size2

        # validate state, and symbols in transition domain
        for x in x_dom:
            assert 0 <= x[0] < num_states
            for a in x[1:self.num_tapes + 1]:
                assert a in self.alphabet

        #  validate state, symbols, and directions in transition range
        for x in x_rng:
            assert 0 <= x[0] < num_states
            for a in x[1:self.num_tapes + 1]:
                assert a in self.alphabet
            for d in x[self.num_tapes + 1:]:
                assert d in self.DIRECTION



    def run(self, tape0):
        """Run simulation.  Only first tape is specified.
        """

        # verify tape symbols
        for sym in tape0:
            assert sym in self.alphabet

        # initialize tapes
        tapes = [list(tape0)]
        for _ in xrange(self.num_tapes - 1):
            tapes.append(["b"])

        # intialize state and head positions
        current_state = self.start
        current_pos = [0] * self.num_tapes

        output = ""

        while True:
            current_syms = self.get_current_syms(current_pos, tapes)

            output += self.display_machine(current_state, current_pos, tapes)

            if current_state in (self.accept, self.reject):
                self.print_configuration(tape0, current_state, output)
                return

            x_dom = tuple([current_state] + current_syms)

            try:
                x_rng = self.transitions[x_dom]
            except KeyError:
                self.print_configuration(tape0, self.reject, output)
                return

            self.write_syms(current_pos, tapes, self.get_syms(x_rng)) 
            try:
                self.verify_heads(current_pos, self.get_dirs(x_rng))
            except AssertionError:
                print("Boundary violation")
                self.print_configuration(tape0, self.reject, output)
                return

            current_pos = self.move_heads(current_pos, self.get_dirs(x_rng))
            current_state = x_rng[0]

    def print_configuration(self, tape0, final_state, output):
        """Output result and sequence of machine configurations.
        """
        if final_state == self.accept:
            action = "accept"
        elif final_state == self.reject:
            action = "reject"
        else:
            raise "unknown action"

        print("You program {}ed {} with the configuration sequence:\n".\
                  format(action, "".join(tape0)))
        print(output)
    
    def get_dirs(self, x_rng):
        """Get the directions from the transition range.
        """
        return x_rng[-self.num_tapes:]

    def get_syms(self, x_rng):
        """Get the symbols from the transition range.
        """
        return x_rng[1:self.num_tapes+1]

    @staticmethod
    def size(states):
        """Verify list of tuples are uniformly sized. Return size.
        """
        nums = set([len(s) for s in states])
        assert len(nums) == 1
        for n in nums:
            return n

    @staticmethod
    def get_current_syms(current_pos, tapes):
        """Get current symbols under tape heads. Append blank when 
        head is at end of tape.
        """
        syms = []

        for p, t in izip(current_pos, tapes):
            assert 0 <= p <= len(t)
            if p == len(t):
                t.append("b")
                syms.append("b")
            else:
                syms.append(t[p])

        return syms

    @staticmethod
    def display_machine(current_state, current_pos, tapes):
        """Display machine state in same format as Udacity simulator.
        """
        state_str = "{{q_{}}}".format(current_state)
        output = ""
        for p, t in izip(current_pos, tapes):
            output += "{}{}{}\n".format("".join(t[:p]), state_str, 
                                        "".join(t[p:]))
        output += "\n"
        return output

    @staticmethod
    def write_syms(current_pos, tapes, syms):
        """Write new symbols to tapes.
        """
        for p, t, s in izip(current_pos, tapes, syms):
            t[p] = s

    @staticmethod
    def verify_heads(current_pos, directions):
        """Verify that tape heads do not attempt to overrun left 
        tape boundary.
        """
        for p, d in izip(current_pos, directions):
            assert p != 0 or d != "L"

    @staticmethod
    def move_heads(current_pos, directions):
        """Move the tape heads.
        """
        next_pos = []
        offset = { "S": 0, "L": -1, "R": 1 }

        for p, d in izip(current_pos, directions):
            try:
                next_pos.append(p + offset[d])
            except KeyError:
                raise "Illegal direction: " + d

        return next_pos