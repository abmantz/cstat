CFLAGS += -O3
AR += -r

.PHONY: default objects archives exe test clean

default: objects archives test

PACKAGE = cstat
ARCHIVES = $(PACKAGE).a
EXES = testexe
OBJECTS = $(foreach s,$(PACKAGE),$(s).o)
ALLOBJECTS = $(OBJECTS) $(foreach s,$(EXES),$(s).o)
TESTOUTPUT = test.png

objects: $(OBJECTS)
archives: $(ARCHIVES)
exe: $(EXES)
test: $(TESTOUTPUT)

$(EXES): $(OBJECTS)

$(ARCHIVES): $(OBJECTS)
	$(RM) $@; $(AR) $@ $?

test.png: testexe
	R --vanilla < test.R

clean:
	$(RM) $(ALLOBJECTS) $(ARCHIVES) $(EXES) $(TESTOUTPUT)
