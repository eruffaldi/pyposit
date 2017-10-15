
D = dlmread('x8.txt');
A= spconvert(D);
assert(size(D,1) == length(unique(1000*D(:,1)+10*D(:,2))),'not unique');
size(D)
size(A)
max(A(:)) % should be 48
spy(A)
surf(full(A))