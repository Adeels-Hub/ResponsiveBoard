In SQL Server:
- Only the **outermost `COMMIT`** actually commits the transaction to the database.    
- Inner `COMMIT`s **do nothing** except decrement an internal counter.    
- If the **outermost transaction fails or is rolled back**, **all changes, including those "committed" in inner transactions, are lost**.
- using `SAVE TRAN SavePoint1` **does NOT allow you to keep inner work if the outer transaction fails**.
<code>
BEGIN TRAN Tran1
    -- Save something       ← saved, but not yet committed

    BEGIN TRAN Tran2
        -- Save something else   ← saved, but also not committed
    COMMIT TRAN Tran2         -- ← just decrements counter, NO actual commit

    -- Save something more   ← saved, still uncommitted

COMMIT TRAN Tran1             -- ← the only real commit

</code>

<code>
BEGIN TRAN

SAVE TRAN SavePoint1
    -- do something risky
    IF @@ERROR <> 0
        ROLLBACK TRAN SavePoint1

-- continue...

COMMIT TRAN  -- If this fails then every thing fails any way
</code>