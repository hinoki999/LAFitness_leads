# LA Fitness Warren Lead Value Analysis

## High-Value Lead Indicators

### 1. New Residents (Highest Priority)
- **Why Valuable**: 
  - Actively establishing new routines
  - No existing gym membership locally
  - Higher conversion probability
- **Data Collection Strategy**:
  - USPS change of address records (monthly batch)
  - Real estate transactions (weekly batch)
  - Rental agreements (property management partnerships)
- **Cost Efficiency**:
  - Batch processing reduces API costs
  - Data remains valuable for 60-90 days
  - One-time pull per address

### 2. Direct Search Intent (High Priority)
- **Why Valuable**:
  - Active interest in fitness
  - Ready to make a decision
  - Time-sensitive leads
- **Data Collection Strategy**:
  - Google Search queries for "gym near me" in Warren
  - Maps searches for fitness centers
  - Competitor location searches
- **API Optimization**:
  - Cache results for 24 hours
  - Focus on evening/weekend searches (peak interest times)
  - Geo-fence to target radius

### 3. Competitor Members (Medium Priority)
- **Why Valuable**:
  - Understanding of gym value
  - Known fitness commitment
  - Price/feature sensitivity
- **Data Collection Strategy**:
  - Review analysis of competitor locations
  - Social media engagement with competitor brands
  - Gym check-in patterns
- **Cost Management**:
  - Weekly competitor analysis
  - Focus on dissatisfaction signals
  - Track membership promotion periods

## API Usage Optimization Plan

### Google Places API
1. **Strategic Timing**
   - Peak search hours (6-8am, 5-8pm)
   - Weekend morning surges
   - Post-holiday periods

2. **Caching Strategy**
   ```python
   cache_durations = {
       'business_listings': '7 days',
       'reviews': '24 hours',
       'search_results': '4 hours'
   }
   ```

3. **Query Optimization**
   - Radius refinement based on conversion data
   - Keyword precision for intent
   - Exclude non-converting demographics

### Cost-Benefit Analysis

#### API Costs vs. Lead Value
```
Monthly Budget Allocation:
- New Resident Data: 50% (Highest ROI)
- Search Intent Tracking: 30% (Time-sensitive)
- Competitor Analysis: 20% (Strategic value)
```

#### Lead Scoring Matrix
```
Lead Score = (Base Value) × Σ(Multipliers)

Base Values:
- New Resident: 100 points
- Direct Search: 80 points
- Competitor Member: 60 points

Multipliers:
- Within 5 miles: 1.5x
- Recent move (<30 days): 2x
- Fitness interest signals: 1.3x
- Income qualification: 1.4x
```

## Implementation Priorities

### Phase 1: New Resident Tracking
1. Set up property record monitoring
2. Create USPS data integration
3. Implement move timing triggers

### Phase 2: Search Intent Capture
1. Configure Google Places API for targeted queries
2. Set up real-time search monitoring
3. Implement intent scoring system

### Phase 3: Competitor Analysis
1. Monitor competitor location activities
2. Track promotion periods
3. Analyze review sentiments

## Success Metrics

### Primary KPIs
1. Cost per Qualified Lead
2. Lead to Tour Conversion Rate
3. Tour to Signup Conversion Rate
4. Customer Acquisition Cost (CAC)
5. Lifetime Value Prediction (LTV)

### Data Quality Metrics
1. Lead Score Accuracy
2. Data Freshness
3. API Cost per Converted Lead
4. Geographic Precision