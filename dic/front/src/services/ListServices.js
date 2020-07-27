import { Candidate } from "../models"


function getCandidates(word) {
    console.log(word)
    let candidates = []
    try {
        const candidates_obj = eel.get_candidates(word)
        for (let candidate of JSON.parse(candidates_obj)) {
            candidates.push(
                new Candidate(candidate.word,
                    candidate.candidate,
                    candidate.translate)
            )
        }
    } catch (e) {
        console.log(e)
        candidates = [
            new Candidate(word, "init2", "訳"),
            new Candidate("initial", "", ""),
            new Candidate("initialization", "", "initialize")
        ]
    }
    return candidates
}

export default {
    getList(word) {
        return getCandidates(word);
    },
};