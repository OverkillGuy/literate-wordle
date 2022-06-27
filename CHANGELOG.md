# Changelog for literate-wordle

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

This project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html), but the narrative piece in
`wordle.org` is considered a central feature, so additions of content to this
file are seen as worth feature-adding (minor) version bumps, regardless of the
code changes being just patching bugs.

## [Unreleased]

<!-- This section kept empty on purpose to help write un-released changelogs. See https://keepachangelog.com/en/1.0.0/#effort for more reasoning.   -->

### Fixed
- Removed unnecessary check for KeyError in scoring bugfix, thanks to
  [@gpiancastelli](https://github.com/gpiancastelli) again for [pointing it out](https://github.com/OverkillGuy/literate-wordle/issues/1#issuecomment-1156974685).


## [1.1.0] - 2022-06-13
### Fixed
- Bug in guess scoring when a letter occurs twice in guess, but only once (second time) in answer, see [bug #1](https://github.com/OverkillGuy/literate-wordle/issues/1). Thanks to [@gpiancastelli](https://github.com/gpiancastelli) for reporting!

### Added
- New "Post-scriptum" section in `wordle.org`, narrating and reflecting about [bug #1](https://github.com/OverkillGuy/literate-wordle/issues/1).


## [1.0.2] - 2022-05-08
### Fixed
- Typo in a source block's caption field.


## [1.0.1] - 2022-05-07
### Added
- New link to website-rendered version of `wordle.org`.
- New docs section "Changelog" including this document.

### Fixed
- Removed hardcoded "perfect score" string in `play_round`.


## [1.0.0] - 2022-05-06
### Added
- New module `literate_wordle`, implementing simple wordle, with narration in
  literate programming style.
