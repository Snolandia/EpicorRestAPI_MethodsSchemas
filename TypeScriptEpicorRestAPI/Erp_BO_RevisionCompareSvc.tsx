import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RevisionCompareSvc
// Description: Revision Compare Bussines Object
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method BomSetDesignatorsChgFlag
   Description: Set Reference Designator change flag
   OperationID: BomSetDesignatorsChgFlag
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/BomSetDesignatorsChgFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BomSetDesignatorsChgFlag(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BomSetDesignatorsChgFlag_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/BomSetDesignatorsChgFlag", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as BomSetDesignatorsChgFlag_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetComparisonWithComparisonTypes
   Description: Performs validations based on comparison types, and performs revision comparison if validations pass
   OperationID: GetComparisonWithComparisonTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetComparisonWithComparisonTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetComparisonWithComparisonTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetComparisonWithComparisonTypes(requestBody:GetComparisonWithComparisonTypes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetComparisonWithComparisonTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/GetComparisonWithComparisonTypes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetComparisonWithComparisonTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetComparison
   OperationID: GetComparison
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetComparison_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetComparison_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetComparison(requestBody:GetComparison_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetComparison_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/GetComparison", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetComparison_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJobMOM
   Description: To retrieve the Assemblies, Materials and Operations that make up the Method of Manufacturing
for the given Job (or optionally, the given assembly within that Job's MOM).
The set of fields in the dataset is NOT COMPLETE, it only contains fields that are in common
with the MOM definitions corresponding to all three of Quote, Job and Part.  (Actually, only
the fields that are present in Vantage 6.10 Revision Compare;  it is possible there are
fields have been omitted.)
   OperationID: GetJobMOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetJobMOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobMOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobMOM(requestBody:GetJobMOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetJobMOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/GetJobMOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetJobMOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartMOM
   Description: To retrieve the Assemblies, Materials and Operations that make up the Method of Manufacturing
for the given Part Revision.
The set of fields in the dataset is NOT COMPLETE, it only contains fields that are in common
with the MOM definitions corresponding to all three of Quote, Job and Part.  (Actually, only
the fields that are present in Vantage 6.10 Revision Compare;  it is possible there are
fields have been omitted.)
   OperationID: GetPartMOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartMOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartMOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartMOM(requestBody:GetPartMOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartMOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/GetPartMOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPartMOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQuoteMOM
   Description: To retrieve the Assemblies, Materials and Operations that make up the Method of Manufacturing
for the given QuoteLine (or optionally, the given assembly within that QuoteLine's MOM).
The set of fields in the dataset is NOT COMPLETE, it only contains fields that are in common
with the MOM definitions corresponding to all three of Quote, Job and Part.  (Actually, only
the fields that are present in Vantage 6.10 Revision Compare;  it is possible there are
fields have been omitted.)
   OperationID: GetQuoteMOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQuoteMOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteMOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuoteMOM(requestBody:GetQuoteMOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQuoteMOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/GetQuoteMOM", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQuoteMOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface BomSetDesignatorsChgFlag_output{
}

export interface Erp_Tablesets_MaterialCompRow{
      /**  1=LeftHandSide/From record is displayed; 2=RightHandSide/To record is displayed; 0=No change: displayed record is both LHS and RHS  */  
   Comparison:number,
      /**  Part number which has its indented bill of materials list created in this file.
It is used to relate all indented BOM Component records to the final end part number which is being viewed.  */  
   EndPartNum:string,
      /**  Revision number of the EndPartNum (see EndPartNum)  */  
   EndRevision:string,
   EndRevisionChg:boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BOMSequence:number,
   BOMStatus:string,
   BOMStatusChg:boolean,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BOMLevel:number,
   BOMLevelChg:boolean,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  The Indented Part Number of the component material record for the related Parent Part.  Ex. ...DCD-100-SP  */  
   IndMtlPartNum:string,
   IndMtlPartNumChg:boolean,
      /**  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  */  
   MtlRevision:string,
   MtlRevisionChg:boolean,
      /**   Describes the material component Part.
Copied from the Part.PartDescription.  */  
   PartDescription:string,
   PartDescriptionChg:boolean,
   QtyPer:number,
   QtyPerChg:boolean,
   QtyRequired:number,
   QtyRequiredChg:boolean,
      /**  Indicates if this is an assembly "ASM" or raw material "Mtl" requirement.  It is set based on the PartRev.PullAsAsm value, Yes = Asm, No = Mtl.  */  
   BOMType:string,
   BOMTypeChg:boolean,
      /**  A factor that multiplied by the QtyRequired results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
   SalvageQtyPerChg:boolean,
      /**  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
   SalvageUnitCreditChg:boolean,
   RelatedOperation:number,
   RelatedOperationChg:boolean,
   UOM:string,
   UOMChg:boolean,
      /**  Reference designators  */  
   Designators:string,
      /**  Reference designators change  */  
   DesignatorsChg:boolean,
   MtlSeq:number,
   MtlSeqChg:boolean,
   DspSequence:number,
      /**  Planning Pct  */  
   PlanningPct:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RevAsmRow{
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BOMSequence:number,
      /**  BOMSequence number of the Parent Assembly.  */  
   ParentBOMSequence:number,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   AsmPartNum:string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   AsmRevisionNum:string,
   AsmAltMethod:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RevComparisonTableset{
   MaterialComp:Erp_Tablesets_MaterialCompRow[],
   RoutingComp:Erp_Tablesets_RoutingCompRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RevDesRow{
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**  A sequence number that uniquely defines the Material record within a specific Job/Part/Quote Assembly.  */  
   BomMtlSequence:number,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  Link to PartMtlRefDes table when available.  */  
   Description:string,
   EndAltMethod:string,
      /**  Part number which has its indented bill of materials list created in this file.  It is used to relate all indented BOM Component records to the final end part number which is being viewed.  */  
   EndPartNum:string,
      /**  Revision number of the EndPartNum (see EndPartNum)  */  
   EndRevision:string,
   MtlPartNum:string,
      /**  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  */  
   MtlRevision:string,
      /**  Link to PartMtlRefDes table when available.  */  
   RefDes:string,
      /**  Link to PartMtlRefDes table when available.  */  
   RefDesSeq:number,
      /**  Link to PartMtlRefDes table when available.  */  
   Rotation:number,
   Side:string,
      /**  Link to PartMtlRefDes table when available.  */  
   XLocation:number,
      /**  Link to PartMtlRefDes table when available.  */  
   YLocation:number,
      /**  Link to PartMtlRefDes table when available.  */  
   ZLocation:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RevMtlRow{
      /**  Part number which has its indented bill of materials list created in this file.
It is used to relate all indented BOM Component records to the final end part number which is being viewed.  */  
   EndPartNum:string,
      /**  Revision number of the EndPartNum (see EndPartNum)  */  
   EndRevision:string,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  A sequence number that uniquely defines the Material record within a specific Job/Part/Quote Assembly.  */  
   BomMtlSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  */  
   MtlRevision:string,
      /**   Describes the material component Part.
Copied from the Part.PartDescription.  */  
   PartDescription:string,
   QtyPer:number,
   QtyRequired:number,
      /**  A factor that multiplied by the QtyRequired results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**   A material record can be related to a specific operation. This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  */  
   RelatedOperation:number,
   EndAltMethod:string,
   RelatedStage:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RevOprRow{
      /**  Part number which has its indented bill of materials list created in this file.
It is used to relate all indented BOM Component records to the final end part number which is being viewed.  */  
   EndPartNum:string,
      /**  Revision number of the EndPartNum (see EndPartNum)  */  
   EndRevision:string,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/Part/Quote Assembly.  */  
   BomOprSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  */  
   MtlRevision:string,
      /**   Describes the material component Part.
Copied from the Part.PartDescription.  */  
   PartDescription:string,
   QtyPer:number,
   QtyRequired:number,
      /**  Indicates if this is an assembly "ASM" or raw material "Mtl" requirement.  It is set based on the PartRev.PullAsAsm value, Yes = Asm, No = Mtl.  */  
   BOMType:string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If l  */  
   OprSeq:number,
      /**  The planned workcenter for this operation. Must  valid in the WrkCenter master file. Links the operation to a WorkCenter master.  */  
   ResourceGrpID:string,
      /**   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalcuate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "O  */  
   EstProdHours:number,
   EndAltMethod:string,
   StageNumber:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RevisionCompareTableset{
   RevAsm:Erp_Tablesets_RevAsmRow[],
   RevMtl:Erp_Tablesets_RevMtlRow[],
   RevOpr:Erp_Tablesets_RevOprRow[],
   RevDes:Erp_Tablesets_RevDesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RoutingCompRow{
      /**  1=LeftHandSide/From record is displayed; 2=RightHandSide/To record is displayed; 0=No change: displayed record is both LHS and RHS  */  
   Comparison:number,
      /**  Part number which has its indented bill of materials list created in this file.
It is used to relate all indented BOM Component records to the final end part number which is being viewed.  */  
   EndPartNum:string,
      /**  Revision number of the EndPartNum (see EndPartNum)  */  
   EndRevision:string,
   EndRevisionChg:boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BOMSequence:number,
   BOMStatus:string,
   BOMStatusChg:boolean,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BOMLevel:number,
   BOMLevelChg:boolean,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  The Indented Part Number of the component material record for the related Parent Part.  Ex. ...DCD-100-SP  */  
   IndMtlPartNum:string,
   IndMtlPartNumChg:boolean,
      /**  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  */  
   MtlRevision:string,
   MtlRevisionChg:boolean,
      /**   Describes the material component Part.
Copied from the Part.PartDescription.  */  
   PartDescription:string,
   PartDescriptionChg:boolean,
   QtyPer:number,
   QtyPerChg:boolean,
   QtyRequired:number,
   QtyRequiredChg:boolean,
      /**  Indicates if this is an assembly "ASM" or raw material "Mtl" requirement.  It is set based on the PartRev.PullAsAsm value, Yes = Asm, No = Mtl.  */  
   BOMType:string,
   BOMTypeChg:boolean,
      /**  The planned ResourceGroup (workcenter) for this operation. Must  valid in the ResourceGroup master file. Links the operation to a ResourceGroup master.  */  
   ResourceGroup:string,
   ResourceGroupChg:boolean,
      /**   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  */  
   OpCode:string,
   OpCodeChg:boolean,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user.  */  
   OprSeq:string,
   OprSeqChg:boolean,
      /**  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  */  
   EstSetHours:number,
   EstSetHoursChg:boolean,
      /**  The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalcuate it  when it is needed.  */  
   EstProdHours:number,
   EstProdHoursChg:boolean,
   DspSequence:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param fromComparison
      @param toComparison
      @param pcMOM1PartNum
      @param pcMOM1RevisionNum
      @param pcMOM1AltMethod
      @param pcMOM1JobNum
      @param piMOM1QuoteNum
      @param piMOM1QuoteLine
      @param piMOM1AssemblySeq
      @param pdMOM1AsOfDate
      @param pcMOM2PartNum
      @param pcMOM2RevisionNum
      @param pcMOM2AltMethod
      @param pcMOM2JobNum
      @param piMOM2QuoteNum
      @param piMOM2QuoteLine
      @param piMOM2AssemblySeq
      @param pdMOM2AsOfDate
   */  
export interface GetComparisonWithComparisonTypes_input{
      /**  Indicates what the from comparison is: Quote, Job, Part  */  
   fromComparison:string,
      /**  Indicates what the to comparison is: Quote, Job, Part  */  
   toComparison:string,
      /**  Item1 Part number (applies to Part comparison).  */  
   pcMOM1PartNum:string,
      /**  Item1 RevisionNum (applies to Part comparison).  */  
   pcMOM1RevisionNum:string,
      /**  (optional) Item1 AltMethod (applies to Part comparison).  */  
   pcMOM1AltMethod:string,
      /**  Item1 JobNum (applies to Job comparison).  */  
   pcMOM1JobNum:string,
      /**  Item1 QuoteNum (applies to Quote comparison).  */  
   piMOM1QuoteNum:number,
      /**  Item1 QuoteLine (applies to Quote comparison).  */  
   piMOM1QuoteLine:number,
      /**  Item1 AssemblySeq (applies to Job or Quote comparison).  */  
   piMOM1AssemblySeq:number,
      /**  (optional) Item1 "as of" date for Revisions to be used (applies to Job or Part comparison).  */  
   pdMOM1AsOfDate:string,
      /**  Item2 Part number (applies to Part comparison).  */  
   pcMOM2PartNum:string,
      /**  Item2 RevisionNum (applies to Part comparison).  */  
   pcMOM2RevisionNum:string,
      /**  (optional) Item2 AltMethod (applies to Part comparison).  */  
   pcMOM2AltMethod:string,
      /**  Item2 JobNum (applies to Job comparison).  */  
   pcMOM2JobNum:string,
      /**  Item2 QuoteNum (applies to Quote comparison).  */  
   piMOM2QuoteNum:number,
      /**  Item2 QuoteLine (applies to Quote comparison).  */  
   piMOM2QuoteLine:number,
      /**  Item2 AssemblySeq (applies to Job or Quote comparison).  */  
   piMOM2AssemblySeq:number,
      /**  (optional) Item2 "as of" date for Revisions to be used (applies to Job or Part comparison).  */  
   pdMOM2AsOfDate:string,
}

export interface GetComparisonWithComparisonTypes_output{
   returnObj:Erp_Tablesets_RevComparisonTableset[],
parameters : {
      /**  output parameters  */  
   pcFrameTitle:string,
}
}

   /** Required : 
      @param pcMOM1PartNum
      @param pcMOM1RevisionNum
      @param pcMOM1AltMethod
      @param pcMOM1JobNum
      @param piMOM1QuoteNum
      @param piMOM1QuoteLine
      @param piMOM1AssemblySeq
      @param pdMOM1AsOfDate
      @param pcMOM2PartNum
      @param pcMOM2RevisionNum
      @param pcMOM2AltMethod
      @param pcMOM2JobNum
      @param piMOM2QuoteNum
      @param piMOM2QuoteLine
      @param piMOM2AssemblySeq
      @param pdMOM2AsOfDate
   */  
export interface GetComparison_input{
      /**  Item1 Part number (applies to Part comparison).  */  
   pcMOM1PartNum:string,
      /**  Item1 RevisionNum (applies to Part comparison).  */  
   pcMOM1RevisionNum:string,
      /**  (optional) Item1 AltMethod (applies to Part comparison).  */  
   pcMOM1AltMethod:string,
      /**  Item1 JobNum (applies to Job comparison).  */  
   pcMOM1JobNum:string,
      /**  Item1 QuoteNum (applies to Quote comparison).  */  
   piMOM1QuoteNum:number,
      /**  Item1 QuoteLine (applies to Quote comparison).  */  
   piMOM1QuoteLine:number,
      /**  Item1 AssemblySeq (applies to Job or Quote comparison).  */  
   piMOM1AssemblySeq:number,
      /**  (optional) Item1 "as of" date for Revisions to be used (applies to Job or Part comparison).  */  
   pdMOM1AsOfDate:string,
      /**  Item2 Part number (applies to Part comparison).  */  
   pcMOM2PartNum:string,
      /**  Item2 RevisionNum (applies to Part comparison).  */  
   pcMOM2RevisionNum:string,
      /**  (optional) Item2 AltMethod (applies to Part comparison).  */  
   pcMOM2AltMethod:string,
      /**  Item2 JobNum (applies to Job comparison).  */  
   pcMOM2JobNum:string,
      /**  Item2 QuoteNum (applies to Quote comparison).  */  
   piMOM2QuoteNum:number,
      /**  Item2 QuoteLine (applies to Quote comparison).  */  
   piMOM2QuoteLine:number,
      /**  Item2 AssemblySeq (applies to Job or Quote comparison).  */  
   piMOM2AssemblySeq:number,
      /**  (optional) Item2 "as of" date for Revisions to be used (applies to Job or Part comparison).  */  
   pdMOM2AsOfDate:string,
}

export interface GetComparison_output{
   returnObj:Erp_Tablesets_RevComparisonTableset[],
parameters : {
      /**  output parameters  */  
   pcFrameTitle:string,
}
}

   /** Required : 
      @param pcJobNum
      @param piAssemblySeq
   */  
export interface GetJobMOM_input{
      /**  Job ID of MOM (Bill of Materials + Bill of Operations) to be retrieved.  */  
   pcJobNum:string,
      /**  (optional) Assembly number of MOM to be retrieved.  */  
   piAssemblySeq:number,
}

export interface GetJobMOM_output{
   returnObj:Erp_Tablesets_RevisionCompareTableset[],
}

   /** Required : 
      @param pcPartNum
      @param pcRevisionNum
      @param pcAltMethod
      @param pdAsOfDate
   */  
export interface GetPartMOM_input{
      /**  Part number of MOM (Bill of Materials + Bill of Operations) to be retrieved.  */  
   pcPartNum:string,
      /**  Revision ID of MOM to be retrieved.  */  
   pcRevisionNum:string,
      /**  Alt Method of MOM to be retrieved.  */  
   pcAltMethod:string,
      /**  (optional) Revisions that were current as of this date to be used.  */  
   pdAsOfDate:string,
}

export interface GetPartMOM_output{
   returnObj:Erp_Tablesets_RevisionCompareTableset[],
}

   /** Required : 
      @param piQuoteNum
      @param piQuoteLine
      @param piAssemblySeq
      @param pdAsOfDate
   */  
export interface GetQuoteMOM_input{
      /**  Quote number of MOM (Bill of Materials + Bill of Operations) to be retrieved.  */  
   piQuoteNum:number,
      /**  Quote Line of MOM to be retrieved.  */  
   piQuoteLine:number,
      /**  (optional) Assembly number of MOM to be retrieved.  */  
   piAssemblySeq:number,
      /**  (optional) Revisions that were current as of this date to be used.  */  
   pdAsOfDate:string,
}

export interface GetQuoteMOM_output{
   returnObj:Erp_Tablesets_RevisionCompareTableset[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

