import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartWipSearchSvc
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartWipSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartWipSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartWipSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWipRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches",headers=creds) as resp:
           return await resp.json()

async def post_PartWipSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartWipSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartWipRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartWipRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartWipSearches_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_PCID_AttributeSetID_SysRowID(Company, Plant, PartNum, JobNum, AssemblySeq, OprSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, MtlSeq, PCID, AttributeSetID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartWipSearch item
   Description: Calls GetByID to retrieve the PartWipSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartWipSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartWipRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + PCID + "," + AttributeSetID + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartWipSearches_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_PCID_AttributeSetID_SysRowID(Company, Plant, PartNum, JobNum, AssemblySeq, OprSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, MtlSeq, PCID, AttributeSetID, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartWipSearch for the service
   Description: Calls UpdateExt to update PartWipSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartWipSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartWipRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + PCID + "," + AttributeSetID + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartWipSearches_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_PCID_AttributeSetID_SysRowID(Company, Plant, PartNum, JobNum, AssemblySeq, OprSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, MtlSeq, PCID, AttributeSetID, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartWipSearch item
   Description: Call UpdateExt to delete PartWipSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartWipSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + PCID + "," + AttributeSetID + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWipListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartWip, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartWip=" + whereClausePartWip
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, partNum, jobNum, assemblySeq, oprSeq, wareHouseCode, binNum, lotNum, dimCode, trackType, mtlSeq, pcID, attributeSetID, sysRowID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "jobNum=" + jobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "assemblySeq=" + assemblySeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "oprSeq=" + oprSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "wareHouseCode=" + wareHouseCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "binNum=" + binNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "lotNum=" + lotNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "dimCode=" + dimCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "trackType=" + trackType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mtlSeq=" + mtlSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pcID=" + pcID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "attributeSetID=" + attributeSetID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysRowID=" + sysRowID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPartWipOprList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartWipOprList
   OperationID: GetPartWipOprList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartWipOprList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartWipOprList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsJobTracker(jobNum, trackType, wipCompleteOnly, excludePartLocations, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsJobTracker
   Description: Returns PartWip records for Job Tracker
   OperationID: Get_GetRowsJobTracker
      :param jobNum: Desc: Job Number   Required: True   Allow empty value : True
      :param trackType: Desc: Track type records to return   Required: True   Allow empty value : True
      :param wipCompleteOnly: Desc: Return only completed for Wip   Required: True
      :param excludePartLocations: Desc: Exclude part locations   Required: True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute Page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsJobTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "jobNum=" + jobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "trackType=" + trackType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "wipCompleteOnly=" + wipCompleteOnly
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "excludePartLocations=" + excludePartLocations
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartWip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartWip
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartWip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartWip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartWip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartWipListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartWipRow] = obj["value"]
      pass

class Erp_Tablesets_PartWipListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.Quantity:int = obj["Quantity"]
      """  Part Quantity balance for a  Job/Asm/Opr at a warehouse/bin location.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  Assembly Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromOprSeq:int = obj["FromOprSeq"]
      """  Operation Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromResourceGrpID:str = obj["FromResourceGrpID"]
      """  Resource Group which created the parts allocated to this operation.  This only pertains to semi-finished manufactured parts (TrackType = M)  """  
      self.FromOpCode:str = obj["FromOpCode"]
      """  Operation Code which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.LastActivityDate:str = obj["LastActivityDate"]
      """  Last Activity Date.  """  
      self.LastActivityTime:int = obj["LastActivityTime"]
      """  Time of last activity expressed in seconds from midnight.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.UpdateStageQty:str = obj["UpdateStageQty"]
      """  Used in the PartWip write trigger to control update to JobMtl.QtyStagedToDate field. Only transactions which  move the material in/out of the staging area update this field.  This field will contain the transaction type that moved the material. For example; STK-MTL(issue of stock), PUR-MTL( movement of purchased material), MTL-STK( Returns to stock).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  ResourceGroup Output Warehouse  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Output BinNum from ResourceGroup  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description  """  
      self.ResGrpDescription:str = obj["ResGrpDescription"]
      """  Resource Group Description  """  
      self.IsDistinct:bool = obj["IsDistinct"]
      """  Tells if the current row is the first occurence for the operation or not.  """  
      self.TranQty:int = obj["TranQty"]
      """  Quantity converted to the TranUOM, which can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  """  
      self.TranUOM:str = obj["TranUOM"]
      """  Can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  """  
      self.JobPartDescription:str = obj["JobPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time and Backflush Qty.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartWipRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.Quantity:int = obj["Quantity"]
      """  Part Quantity balance for a  Job/Asm/Opr at a warehouse/bin location.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  Assembly Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromOprSeq:int = obj["FromOprSeq"]
      """  Operation Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromResourceGrpID:str = obj["FromResourceGrpID"]
      """  Resource Group which created the parts allocated to this operation.  This only pertains to semi-finished manufactured parts (TrackType = M)  """  
      self.FromOpCode:str = obj["FromOpCode"]
      """  Operation Code which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.LastActivityDate:str = obj["LastActivityDate"]
      """  Last Activity Date.  """  
      self.LastActivityTime:int = obj["LastActivityTime"]
      """  Time of last activity expressed in seconds from midnight.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.UpdateStageQty:str = obj["UpdateStageQty"]
      """  Used in the PartWip write trigger to control update to JobMtl.QtyStagedToDate field. Only transactions which  move the material in/out of the staging area update this field.  This field will contain the transaction type that moved the material. For example; STK-MTL(issue of stock), PUR-MTL( movement of purchased material), MTL-STK( Returns to stock).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time and Backflush Qty.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Output BinNum from ResourceGroup  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  ResourceGroup Output Warehouse  """  
      self.ResGrpDescription:str = obj["ResGrpDescription"]
      """  Resource Group Description  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.TranQty:int = obj["TranQty"]
      """  Quantity converted to the TranUOM, which can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  """  
      self.TranUOM:str = obj["TranUOM"]
      """  Can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  """  
      self.IsDistinct:bool = obj["IsDistinct"]
      """  Tells if the current row is the first occurence for the operation or not.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobPartDescription:str = obj["JobPartDescription"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   partNum
   jobNum
   assemblySeq
   oprSeq
   wareHouseCode
   binNum
   lotNum
   dimCode
   trackType
   mtlSeq
   pcID
   attributeSetID
   sysRowID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.partNum:str = obj["partNum"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.wareHouseCode:str = obj["wareHouseCode"]
      self.binNum:str = obj["binNum"]
      self.lotNum:str = obj["lotNum"]
      self.dimCode:str = obj["dimCode"]
      self.trackType:str = obj["trackType"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.pcID:str = obj["pcID"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.sysRowID:str = obj["sysRowID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartWipListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.Quantity:int = obj["Quantity"]
      """  Part Quantity balance for a  Job/Asm/Opr at a warehouse/bin location.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  Assembly Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromOprSeq:int = obj["FromOprSeq"]
      """  Operation Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromResourceGrpID:str = obj["FromResourceGrpID"]
      """  Resource Group which created the parts allocated to this operation.  This only pertains to semi-finished manufactured parts (TrackType = M)  """  
      self.FromOpCode:str = obj["FromOpCode"]
      """  Operation Code which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.LastActivityDate:str = obj["LastActivityDate"]
      """  Last Activity Date.  """  
      self.LastActivityTime:int = obj["LastActivityTime"]
      """  Time of last activity expressed in seconds from midnight.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.UpdateStageQty:str = obj["UpdateStageQty"]
      """  Used in the PartWip write trigger to control update to JobMtl.QtyStagedToDate field. Only transactions which  move the material in/out of the staging area update this field.  This field will contain the transaction type that moved the material. For example; STK-MTL(issue of stock), PUR-MTL( movement of purchased material), MTL-STK( Returns to stock).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  ResourceGroup Output Warehouse  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Output BinNum from ResourceGroup  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description  """  
      self.ResGrpDescription:str = obj["ResGrpDescription"]
      """  Resource Group Description  """  
      self.IsDistinct:bool = obj["IsDistinct"]
      """  Tells if the current row is the first occurence for the operation or not.  """  
      self.TranQty:int = obj["TranQty"]
      """  Quantity converted to the TranUOM, which can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  """  
      self.TranUOM:str = obj["TranUOM"]
      """  Can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  """  
      self.JobPartDescription:str = obj["JobPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time and Backflush Qty.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartWipListTableset:
   def __init__(self, obj):
      self.PartWipList:list[Erp_Tablesets_PartWipListRow] = obj["PartWipList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartWipRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.Quantity:int = obj["Quantity"]
      """  Part Quantity balance for a  Job/Asm/Opr at a warehouse/bin location.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  Assembly Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromOprSeq:int = obj["FromOprSeq"]
      """  Operation Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromResourceGrpID:str = obj["FromResourceGrpID"]
      """  Resource Group which created the parts allocated to this operation.  This only pertains to semi-finished manufactured parts (TrackType = M)  """  
      self.FromOpCode:str = obj["FromOpCode"]
      """  Operation Code which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.LastActivityDate:str = obj["LastActivityDate"]
      """  Last Activity Date.  """  
      self.LastActivityTime:int = obj["LastActivityTime"]
      """  Time of last activity expressed in seconds from midnight.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.UpdateStageQty:str = obj["UpdateStageQty"]
      """  Used in the PartWip write trigger to control update to JobMtl.QtyStagedToDate field. Only transactions which  move the material in/out of the staging area update this field.  This field will contain the transaction type that moved the material. For example; STK-MTL(issue of stock), PUR-MTL( movement of purchased material), MTL-STK( Returns to stock).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time and Backflush Qty.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Output BinNum from ResourceGroup  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  ResourceGroup Output Warehouse  """  
      self.ResGrpDescription:str = obj["ResGrpDescription"]
      """  Resource Group Description  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.TranQty:int = obj["TranQty"]
      """  Quantity converted to the TranUOM, which can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  """  
      self.TranUOM:str = obj["TranUOM"]
      """  Can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  """  
      self.IsDistinct:bool = obj["IsDistinct"]
      """  Tells if the current row is the first occurence for the operation or not.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobPartDescription:str = obj["JobPartDescription"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartWipSearchTableset:
   def __init__(self, obj):
      self.PartWip:list[Erp_Tablesets_PartWipRow] = obj["PartWip"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartWipSearchTableset:
   def __init__(self, obj):
      self.PartWip:list[Erp_Tablesets_PartWipRow] = obj["PartWip"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   partNum
   jobNum
   assemblySeq
   oprSeq
   wareHouseCode
   binNum
   lotNum
   dimCode
   trackType
   mtlSeq
   pcID
   attributeSetID
   sysRowID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.partNum:str = obj["partNum"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.wareHouseCode:str = obj["wareHouseCode"]
      self.binNum:str = obj["binNum"]
      self.lotNum:str = obj["lotNum"]
      self.dimCode:str = obj["dimCode"]
      self.trackType:str = obj["trackType"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.pcID:str = obj["pcID"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.sysRowID:str = obj["sysRowID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWipSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWipSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWipSearchTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWipListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartWip_input:
   """ Required : 
   ds
   plant
   partNum
   jobNum
   assemblySeq
   oprSeq
   wareHouseCode
   binNum
   lotNum
   dimCode
   trackType
   mtlSeq
   pcID
   attributeSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartWipSearchTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.partNum:str = obj["partNum"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.wareHouseCode:str = obj["wareHouseCode"]
      self.binNum:str = obj["binNum"]
      self.lotNum:str = obj["lotNum"]
      self.dimCode:str = obj["dimCode"]
      self.trackType:str = obj["trackType"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.pcID:str = obj["pcID"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetNewPartWip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartWipSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartWipOprList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetPartWipOprList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWipListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsJobTracker_input:
   """ Required : 
   jobNum
   trackType
   wipCompleteOnly
   excludePartLocations
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      self.trackType:str = obj["trackType"]
      """  Track type records to return  """  
      self.wipCompleteOnly:bool = obj["wipCompleteOnly"]
      """  Return only completed for Wip  """  
      self.excludePartLocations:bool = obj["excludePartLocations"]
      """  Exclude part locations  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsJobTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWipSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartWip
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartWip:str = obj["whereClausePartWip"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWipSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartWipSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartWipSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartWipSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartWipSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

