import { Candidate } from "../models"


async function getCandidates(word) {
    console.log(word)
    let candidates = []
    try {
        let candidates_obj = await eel.get_candidates(word)()
        for (let candidate of JSON.parse(candidates_obj)) {
            console.log(candidate.word)
            candidates.push(
                new Candidate(candidate.word,
                    candidate.candidate,
                    candidate.translate)
            )
        }
        return candidates
    } catch (e) {
        console.log(e)
        candidates = [
            new Candidate(word, "init2", "訳"),
            new Candidate("initial", "", ""),
            new Candidate("initialization", "", "initialize")
        ]
        return candidates
    }

}

export default {
    getList(word) {
        return getCandidates(word);
    },
};