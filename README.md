# Democratic p-values

## Background

See the history for why I'm not entirely sure. But there are three primary plots being made here. The idea being that if you obtain significances from two different experiments and you want to combine them in a way to make a statement about them, you can combine them "democratically". As [@cranmer](https://github.com/cranmer) states, there are an infinite number of ways to combine p-values, there is no "right way" as it's an under-specified problem.

- `hdp0` is a plot that shows the combined significance
- `hsqd` shows the standard quadrature sum

## History

huh? Anyway, [@mhance](https://github.com/mhance) emailed me back in November 23rd, 2018 around 6am about this. He sent me an email with a single [attachment](./democratic_pvalues_pyroot.py) which used [ROOT](https://root.cern/) to compute a bunch of things and make three canvases ([hdp0](./hdp0.pdf), [hsqd](./hsqd.pdf), [hdif](./hdif.pdf)).

For a long time, it was on my to-do list to convert this into equivalent [numpy](https://numpy.org/) and [scipy](https://scipy.org/) code and maybe glean some understanding. However, now that I'm getting around to this, I don't know why this came up, or why Mike sent this to me. I asked him, and he vaguely recalls a presentation on this, but it never came up again.

Anyways, this repository is just so I can get closer to [#inboxZero](http://www.43folders.com/43-folders-series-inbox-zero) and achieve nirvana? Maybe? Who knows.
