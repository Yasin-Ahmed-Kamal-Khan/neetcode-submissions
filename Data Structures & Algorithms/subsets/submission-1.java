public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        return helper(Arrays.stream(nums).boxed().toList());
    }

    private List<List<Integer>> helper(List<Integer> nums) {
        List<List<Integer>> bigList = new ArrayList<>();
        for (var num : nums) {
            List<List<Integer>> newBigList = new ArrayList<>(
                bigList.stream()
                    .map(list -> {
                        var newList = new ArrayList<>(list);
                        newList.add(num);
                        return newList;
                    }).toList());

            bigList.addAll(newBigList);
            bigList.add(new ArrayList<>(List.of(num)));
            System.out.println(num);
            System.out.println(bigList);
        }
        bigList.add(List.of());

        return bigList;
    }
}