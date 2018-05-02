CFLAGS += -O3
AR += -r

.PHONY: default objects archives exe test clean

default: objects archives test

PACKAGE = cstat
ARCHIVES = $(PACKAGE).a
EXES = testexe
OBJECTS = $(foreach s,$(PACKAGE),$(s).o)
ALLOBJECTS = $(OBJECTS) $(foreach s,$(EXES),$(s).o)

objects: $(OBJECTS)
archives: $(ARCHIVES)
exe: $(EXES)
test: exe
	./testexe > test.dat && python test.py

$(EXES): $(OBJECTS)

$(ARCHIVES): $(OBJECTS)
	$(RM) $@; $(AR) $@ $?

clean:
	$(RM) $(ALLOBJECTS) $(ARCHIVES) $(EXES)
