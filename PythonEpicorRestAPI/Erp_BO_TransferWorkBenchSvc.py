import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TransferWorkBenchSvc
# Description: The TransferWorkBench object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TransferWorkBenches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TransferWorkBenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransferWorkBenches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches",headers=creds) as resp:
           return await resp.json()

async def post_TransferWorkBenches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TransferWorkBenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TransferWorkBenches_Company_TFLineNum(Company, TFLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TransferWorkBench item
   Description: Calls GetByID to retrieve the TransferWorkBench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransferWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFLineNum: Desc: TFLineNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches(" + Company + "," + TFLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TransferWorkBenches_Company_TFLineNum(Company, TFLineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TransferWorkBench for the service
   Description: Calls UpdateExt to update TransferWorkBench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransferWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFLineNum: Desc: TFLineNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches(" + Company + "," + TFLineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TransferWorkBenches_Company_TFLineNum(Company, TFLineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TransferWorkBench item
   Description: Call UpdateExt to delete TransferWorkBench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransferWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFLineNum: Desc: TFLineNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/TransferWorkBenches(" + Company + "," + TFLineNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTFOrdDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTFOrdDtl=" + whereClauseTFOrdDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tfLineNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "tfLineNum=" + tfLineNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: Find part.
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   Description: Get Part From RowID.
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsForLandingPage(inTFLineList, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForLandingPage
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRowsForLandingPage
      :param inTFLineList: Desc: RowType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "inTFLineList=" + inTFLineList

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetTransferShipDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransferShipDate
   Description: Sets the transfer ship date base on fromplant, toplant, and needbydate.
It's calculated using the needby date and subtracting the transfers days
held in the PltTranDef Table.
   OperationID: GetTransferShipDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransferShipDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferShipDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFirmSuggestion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFirmSuggestion
   Description: This method is called when the Firm checkbox changes
   OperationID: OnChangeFirmSuggestion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFirmSuggestion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFirmSuggestion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: This method is to be called when the Part Number field changes
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQtyValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQtyValue
   Description: This method is called when the Quantity or Quantity UOM changes to convert quantities.
   OperationID: OnChangeQtyValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQtyValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQtyValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingPlant
   Description: Purpose:
Parameters:  none
Notes:
<param name="plantID">PlantID </param><param name="success">Success </param>
   OperationID: OnChangingPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessNewSuggestions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessNewSuggestions
   Description: This method converts unfirm to firm requirements, creates transfer orders .
The suggested where clause:
where TFOrdDtl.Plant  = ipPlant and TFOrdDtl.ToPlant = cur-plant
and TFOrdDtl.NeedByDate less or = horizonDate and TFOrdDtl.TFOrdNum = "":U
and TFOrdDtl.Shipped = no
   OperationID: ProcessNewSuggestions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessNewSuggestions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessNewSuggestions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetDefaultShipVia(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetDefaultShipVia
   Description: This method is to be called when the CreateOrder field changes
   OperationID: SetDefaultShipVia
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDefaultShipVia_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDefaultShipVia_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFOrdDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFOrdDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFOrdDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFOrdDtlRow] = obj["value"]
      pass

class Erp_Tablesets_TFOrdDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.OrderFirm:bool = obj["OrderFirm"]
      """  Indicates an Unfirm Transfer Order.  Similar to JobFirm  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ManualOrder:bool = obj["ManualOrder"]
      """  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job number of the job supplying the parts for this record (FromSite)  """  
      self.DemandJobNum:str = obj["DemandJobNum"]
      """  Job number of the job demand for the parts on this record (ToSite)  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity  """  
      self.AdditionalQty:int = obj["AdditionalQty"]
      """  Additional quantity beyond the initial requirement to be transferred  """  
      self.FirmDate:str = obj["FirmDate"]
      """  Date transfer suggestion went firm  """  
      self.FirmUser:str = obj["FirmUser"]
      """  User who made the transfer suggestion firm  """  
      self.DemandAsmSeq:int = obj["DemandAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.DemandMtlSeq:int = obj["DemandMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SupplyAsmSeq:int = obj["SupplyAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.SupplyMtlSeq:int = obj["SupplyMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.StockTrans:bool = obj["StockTrans"]
      """  Indicates if this requirement/receipt affects stock.  """  
      self.OurStockQtyUOM:str = obj["OurStockQtyUOM"]
      """   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQtyUOM:str = obj["SellingQtyUOM"]
      """   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQty:int = obj["SellingQty"]
      """  Selling Quantity  """  
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      """  Selling Shipped Quantity  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.Selected:bool = obj["Selected"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.CreateOrder:bool = obj["CreateOrder"]
      self.LineStatus:str = obj["LineStatus"]
      """  Descriptive Text of OpenLine Field  """  
      self.LotNum:str = obj["LotNum"]
      self.DimCode:str = obj["DimCode"]
      self.Weight:int = obj["Weight"]
      self.TotNetWeight:int = obj["TotNetWeight"]
      self.BinNum:str = obj["BinNum"]
      self.PkgClass:str = obj["PkgClass"]
      self.PkgCode:str = obj["PkgCode"]
      self.Packages:int = obj["Packages"]
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DUM:str = obj["DUM"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  DimCodeDimCodeDescription  """  
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      """  PkgClassDescription  """  
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  PkgCodeDescription  """  
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockQty * DimConvFactor  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Transfer Order Detail is allocated against.  """  
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  This order inventory quantity  """  
      self.PartDescIUM:str = obj["PartDescIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartDescSalesUM:str = obj["PartDescSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartDescTrackLots:bool = obj["PartDescTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartDescPartDescription:str = obj["PartDescPartDescription"]
      """  Describes the Part.  """  
      self.PartDescSellingFactor:int = obj["PartDescSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartDescTrackSerialNum:bool = obj["PartDescTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartDescPricePerCode:str = obj["PartDescPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartDescTrackDimension:bool = obj["PartDescTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.StageWhseCodeDescription:str = obj["StageWhseCodeDescription"]
      """  Description.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFOrdDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.OrderFirm:bool = obj["OrderFirm"]
      """  Indicates an Unfirm Transfer Order.  Similar to JobFirm  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ManualOrder:bool = obj["ManualOrder"]
      """  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job number of the job supplying the parts for this record (FromSite)  """  
      self.DemandJobNum:str = obj["DemandJobNum"]
      """  Job number of the job demand for the parts on this record (ToSite)  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity  """  
      self.AdditionalQty:int = obj["AdditionalQty"]
      """  Additional quantity beyond the initial requirement to be transferred  """  
      self.FirmDate:str = obj["FirmDate"]
      """  Date transfer suggestion went firm  """  
      self.FirmUser:str = obj["FirmUser"]
      """  User who made the transfer suggestion firm  """  
      self.DemandAsmSeq:int = obj["DemandAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.DemandMtlSeq:int = obj["DemandMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SupplyAsmSeq:int = obj["SupplyAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.SupplyMtlSeq:int = obj["SupplyMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.StockTrans:bool = obj["StockTrans"]
      """  Indicates if this requirement/receipt affects stock.  """  
      self.OurStockQtyUOM:str = obj["OurStockQtyUOM"]
      """   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQtyUOM:str = obj["SellingQtyUOM"]
      """   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQty:int = obj["SellingQty"]
      """  Selling Quantity  """  
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      """  Selling Shipped Quantity  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.TransferContractID:str = obj["TransferContractID"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  """  
      self.TransferLinkToContract:bool = obj["TransferLinkToContract"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the transfer order line should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the transfer order line is ready to be fulfilled.  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      self.BinNum:str = obj["BinNum"]
      self.DimCode:str = obj["DimCode"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  DimCodeDimCodeDescription  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockQty * DimConvFactor  """  
      self.DUM:str = obj["DUM"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Transfer Order Detail is allocated against.  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Descriptive Text of OpenLine Field  """  
      self.LotNum:str = obj["LotNum"]
      self.Packages:int = obj["Packages"]
      self.PCID:str = obj["PCID"]
      self.PkgClass:str = obj["PkgClass"]
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      """  PkgClassDescription  """  
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  PkgCodeDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      self.Selected:bool = obj["Selected"]
      self.StagingBinDesc:str = obj["StagingBinDesc"]
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  This order inventory quantity  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.TotNetWeight:int = obj["TotNetWeight"]
      self.Weight:int = obj["Weight"]
      self.CreateOrder:bool = obj["CreateOrder"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this release is in the fulfillment queue.  """  
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PartDescTrackInventoryAttributes:bool = obj["PartDescTrackInventoryAttributes"]
      self.PartDescAttrClassID:str = obj["PartDescAttrClassID"]
      self.PartDescPricePerCode:str = obj["PartDescPricePerCode"]
      self.PartDescTrackSerialNum:bool = obj["PartDescTrackSerialNum"]
      self.PartDescPartDescription:str = obj["PartDescPartDescription"]
      self.PartDescTrackDimension:bool = obj["PartDescTrackDimension"]
      self.PartDescSalesUM:str = obj["PartDescSalesUM"]
      self.PartDescIUM:str = obj["PartDescIUM"]
      self.PartDescSellingFactor:int = obj["PartDescSellingFactor"]
      self.PartDescTrackLots:bool = obj["PartDescTrackLots"]
      self.PartDescTrackInventoryByRevision:bool = obj["PartDescTrackInventoryByRevision"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.StageWhseCodeDescription:str = obj["StageWhseCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tfLineNum
   """  
   def __init__(self, obj):
      self.tfLineNum:str = obj["tfLineNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TFOrdDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.OrderFirm:bool = obj["OrderFirm"]
      """  Indicates an Unfirm Transfer Order.  Similar to JobFirm  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ManualOrder:bool = obj["ManualOrder"]
      """  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job number of the job supplying the parts for this record (FromSite)  """  
      self.DemandJobNum:str = obj["DemandJobNum"]
      """  Job number of the job demand for the parts on this record (ToSite)  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity  """  
      self.AdditionalQty:int = obj["AdditionalQty"]
      """  Additional quantity beyond the initial requirement to be transferred  """  
      self.FirmDate:str = obj["FirmDate"]
      """  Date transfer suggestion went firm  """  
      self.FirmUser:str = obj["FirmUser"]
      """  User who made the transfer suggestion firm  """  
      self.DemandAsmSeq:int = obj["DemandAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.DemandMtlSeq:int = obj["DemandMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SupplyAsmSeq:int = obj["SupplyAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.SupplyMtlSeq:int = obj["SupplyMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.StockTrans:bool = obj["StockTrans"]
      """  Indicates if this requirement/receipt affects stock.  """  
      self.OurStockQtyUOM:str = obj["OurStockQtyUOM"]
      """   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQtyUOM:str = obj["SellingQtyUOM"]
      """   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQty:int = obj["SellingQty"]
      """  Selling Quantity  """  
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      """  Selling Shipped Quantity  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.Selected:bool = obj["Selected"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.CreateOrder:bool = obj["CreateOrder"]
      self.LineStatus:str = obj["LineStatus"]
      """  Descriptive Text of OpenLine Field  """  
      self.LotNum:str = obj["LotNum"]
      self.DimCode:str = obj["DimCode"]
      self.Weight:int = obj["Weight"]
      self.TotNetWeight:int = obj["TotNetWeight"]
      self.BinNum:str = obj["BinNum"]
      self.PkgClass:str = obj["PkgClass"]
      self.PkgCode:str = obj["PkgCode"]
      self.Packages:int = obj["Packages"]
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DUM:str = obj["DUM"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  DimCodeDimCodeDescription  """  
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      """  PkgClassDescription  """  
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  PkgCodeDescription  """  
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockQty * DimConvFactor  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Transfer Order Detail is allocated against.  """  
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  This order inventory quantity  """  
      self.PartDescIUM:str = obj["PartDescIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartDescSalesUM:str = obj["PartDescSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartDescTrackLots:bool = obj["PartDescTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartDescPartDescription:str = obj["PartDescPartDescription"]
      """  Describes the Part.  """  
      self.PartDescSellingFactor:int = obj["PartDescSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartDescTrackSerialNum:bool = obj["PartDescTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartDescPricePerCode:str = obj["PartDescPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartDescTrackDimension:bool = obj["PartDescTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.StageWhseCodeDescription:str = obj["StageWhseCodeDescription"]
      """  Description.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFOrdDtlListTableset:
   def __init__(self, obj):
      self.TFOrdDtlList:list[Erp_Tablesets_TFOrdDtlListRow] = obj["TFOrdDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TFOrdDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.OrderFirm:bool = obj["OrderFirm"]
      """  Indicates an Unfirm Transfer Order.  Similar to JobFirm  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ManualOrder:bool = obj["ManualOrder"]
      """  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job number of the job supplying the parts for this record (FromSite)  """  
      self.DemandJobNum:str = obj["DemandJobNum"]
      """  Job number of the job demand for the parts on this record (ToSite)  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity  """  
      self.AdditionalQty:int = obj["AdditionalQty"]
      """  Additional quantity beyond the initial requirement to be transferred  """  
      self.FirmDate:str = obj["FirmDate"]
      """  Date transfer suggestion went firm  """  
      self.FirmUser:str = obj["FirmUser"]
      """  User who made the transfer suggestion firm  """  
      self.DemandAsmSeq:int = obj["DemandAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.DemandMtlSeq:int = obj["DemandMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SupplyAsmSeq:int = obj["SupplyAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.SupplyMtlSeq:int = obj["SupplyMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.StockTrans:bool = obj["StockTrans"]
      """  Indicates if this requirement/receipt affects stock.  """  
      self.OurStockQtyUOM:str = obj["OurStockQtyUOM"]
      """   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQtyUOM:str = obj["SellingQtyUOM"]
      """   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQty:int = obj["SellingQty"]
      """  Selling Quantity  """  
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      """  Selling Shipped Quantity  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.TransferContractID:str = obj["TransferContractID"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  """  
      self.TransferLinkToContract:bool = obj["TransferLinkToContract"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the transfer order line should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the transfer order line is ready to be fulfilled.  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      self.BinNum:str = obj["BinNum"]
      self.DimCode:str = obj["DimCode"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  DimCodeDimCodeDescription  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockQty * DimConvFactor  """  
      self.DUM:str = obj["DUM"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Transfer Order Detail is allocated against.  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Descriptive Text of OpenLine Field  """  
      self.LotNum:str = obj["LotNum"]
      self.Packages:int = obj["Packages"]
      self.PCID:str = obj["PCID"]
      self.PkgClass:str = obj["PkgClass"]
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      """  PkgClassDescription  """  
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  PkgCodeDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      self.Selected:bool = obj["Selected"]
      self.StagingBinDesc:str = obj["StagingBinDesc"]
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  This order inventory quantity  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.TotNetWeight:int = obj["TotNetWeight"]
      self.Weight:int = obj["Weight"]
      self.CreateOrder:bool = obj["CreateOrder"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this release is in the fulfillment queue.  """  
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PartDescTrackInventoryAttributes:bool = obj["PartDescTrackInventoryAttributes"]
      self.PartDescAttrClassID:str = obj["PartDescAttrClassID"]
      self.PartDescPricePerCode:str = obj["PartDescPricePerCode"]
      self.PartDescTrackSerialNum:bool = obj["PartDescTrackSerialNum"]
      self.PartDescPartDescription:str = obj["PartDescPartDescription"]
      self.PartDescTrackDimension:bool = obj["PartDescTrackDimension"]
      self.PartDescSalesUM:str = obj["PartDescSalesUM"]
      self.PartDescIUM:str = obj["PartDescIUM"]
      self.PartDescSellingFactor:int = obj["PartDescSellingFactor"]
      self.PartDescTrackLots:bool = obj["PartDescTrackLots"]
      self.PartDescTrackInventoryByRevision:bool = obj["PartDescTrackInventoryByRevision"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.StageWhseCodeDescription:str = obj["StageWhseCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TransferWorkBenchTableset:
   def __init__(self, obj):
      self.TFOrdDtl:list[Erp_Tablesets_TFOrdDtlRow] = obj["TFOrdDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTransferWorkBenchTableset:
   def __init__(self, obj):
      self.TFOrdDtl:list[Erp_Tablesets_TFOrdDtlRow] = obj["TFOrdDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  PartNum  """  
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   tfLineNum
   """  
   def __init__(self, obj):
      self.tfLineNum:str = obj["tfLineNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  TableName  """  
      self.fieldName:str = obj["fieldName"]
      """  FieldName  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TFOrdDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTFOrdDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class GetNewTFOrdDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      """  RowType  """  
      self.ipRowID:str = obj["ipRowID"]
      """  RowID  """  
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsForLandingPage_input:
   """ Required : 
   inTFLineList
   """  
   def __init__(self, obj):
      self.inTFLineList:str = obj["inTFLineList"]
      """  RowType  """  
      pass

class GetRowsForLandingPage_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseTFOrdDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTFOrdDtl:str = obj["whereClauseTFOrdDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTransferShipDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class GetTransferShipDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
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

class OnChangeFirmSuggestion_input:
   """ Required : 
   ipOrderFirm
   ds
   """  
   def __init__(self, obj):
      self.ipOrderFirm:bool = obj["ipOrderFirm"]
      """  OrderFirm  """  
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class OnChangeFirmSuggestion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ds
   partNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      self.partNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class OnChangeQtyValue_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class OnChangeQtyValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingPlant_input:
   """ Required : 
   plantID
   """  
   def __init__(self, obj):
      self.plantID:str = obj["plantID"]
      pass

class OnChangingPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.success:bool = obj["success"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessNewSuggestions_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class ProcessNewSuggestions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetDefaultShipVia_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class SetDefaultShipVia_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTransferWorkBenchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTransferWorkBenchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

