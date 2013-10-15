These questions examine your knowledge of systems programming, operating
systems, and computer architecture. They should be useful when interviewing
for positions that will require writing low-level code.

# Memory Management

## Question 1

What does the following C code do?

    int main(void) {
        int *x = NULL;
        int y = *x;
    }

Explain in as much detail as possible what happens in the processor,
OS kernel, and userspace when this code is executed.

## Question 2

Two separate Linux processes attempt to access memory at the same address,
will these processes interfere with each other? Why or why not?

## Question 3

Explain in as much detail as possible how modern operating systems handle
getting requests for more memory than is available on the machine.

## Question 4

Given the following two programs which are equivalent in functionality,
which one do you expect to run faster and why?

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            sum += arr[i];
        }
    }

    for (j = 0; j < M; j++) {
        for (i = 0; i < N; i++) {
            sum += arr[i];
        }
    }

# Synchronization

## Question 1

Compare-and-swap is an atomic operation supplied by many CPUs to allow
implementation of more complex synchronization primitives.
Compare-and-swap takes a memory region to be updated, the expected value
of that region, and a new value. It will atomically examine the current
contents of memory and, if it is the same as the expected value, update
the memory region with the new value. It then returns the value that was
read from memory.

The following C-like pseudocode explains what compare-and-swap does.

    int compare_and_swap(int *p, int oldval, int newval)
    {
        int curval = *p;
        if (curval == oldval) {
            *p = newval;
        }
        return curval;
    }

Using the compare-and-swap function, please explain how you would implement
a basic `lock` and `unlock` function. The `lock` function takes an integer
pointer (the lock object) can be called from any number of threads.
Only one thread should be allowed to progress past the lock function at
a time. The thread will hold the lock until it calls `unlock` to release it.
So, for instance, I would expect the following code to work as expected
without race conditions when it is run using multiple threads.

    lock(lck);
    /* --- critical section --- */
    unlock(lck);

## Question 2

Given a working `lock` and `unlock` function, explain what the problem is
with the following multi-threaded code and how you would correct it.

In thread A

    lock(lckA);
    lock(lckB);
    /* --- critical section --- */
    unlock(lckA);
    unlock(lckB);

In thread B

    lock(lckB);
    lock(lckA);
    /* --- critical section --- */
    unlock(lckA);
    unlock(lckB);

## Question 3

Explain what a semaphore is and how you would implement it using our
`lock` and `unlock` functions.
