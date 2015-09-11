% Octave has no intdump, its useful in a demodulator.
function [DATA] = intdump(IN, num)
        outidx = 1;
        for (z=1:num:length(IN))
                DATA(outidx) = sum(IN(z:z+num-1));
                outidx = outidx + 1;
        end

% return DATA
end
