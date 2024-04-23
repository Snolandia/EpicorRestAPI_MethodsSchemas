import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.POSuggSvc
# Description: This object Generates PO Suggestions.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_POSuggs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POSuggs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POSuggs
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPoDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs",headers=creds) as resp:
           return await resp.json()

async def post_POSuggs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POSuggs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SugPoDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SugPoDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POSuggs_Company_SugNum(Company, SugNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POSugg item
   Description: Calls GetByID to retrieve the POSugg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POSugg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SugPoDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POSuggs_Company_SugNum(Company, SugNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POSugg for the service
   Description: Calls UpdateExt to update POSugg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POSugg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SugPoDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POSuggs_Company_SugNum(Company, SugNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POSugg item
   Description: Call UpdateExt to delete POSugg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POSugg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_POSuggs_Company_SugNum_SugPoMscs(Company, SugNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SugPoMscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SugPoMscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPoMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")/SugPoMscs",headers=creds) as resp:
           return await resp.json()

async def get_POSuggs_Company_SugNum_SugPoMscs_Company_SugNum_SeqNum(Company, SugNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SugPoMsc item
   Description: Calls GetByID to retrieve the SugPoMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SugPoMsc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SugPoMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/POSuggs(" + Company + "," + SugNum + ")/SugPoMscs(" + Company + "," + SugNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SugPoMscs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SugPoMscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SugPoMscs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPoMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs",headers=creds) as resp:
           return await resp.json()

async def post_SugPoMscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SugPoMscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SugPoMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SugPoMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SugPoMscs_Company_SugNum_SeqNum(Company, SugNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SugPoMsc item
   Description: Calls GetByID to retrieve the SugPoMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SugPoMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SugPoMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs(" + Company + "," + SugNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SugPoMscs_Company_SugNum_SeqNum(Company, SugNum, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SugPoMsc for the service
   Description: Calls UpdateExt to update SugPoMsc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SugPoMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SugPoMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs(" + Company + "," + SugNum + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SugPoMscs_Company_SugNum_SeqNum(Company, SugNum, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SugPoMsc item
   Description: Call UpdateExt to delete SugPoMsc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SugPoMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/SugPoMscs(" + Company + "," + SugNum + "," + SeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPoDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSugPoDtl, whereClauseSugPoMsc, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseSugPoDtl=" + whereClauseSugPoDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSugPoMsc=" + whereClauseSugPoMsc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sugNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "sugNum=" + sugNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Autoselect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Autoselect
   Description: This method will automatically change the Buy specification to Yes for any suggestion
for the currently selected buyer that spicifies a vendor, a unit price a quantity , a purchasing factor
and a unit of measure .
            
The UI must mark the selected ttSugPoDtl records are "dirty" before calling this
method.  This is to allow auto select to only run on the records selected
            
This is a danger that there will be some records selected that will not show up in this dataset.
These records may have been updated using a previous filter ( or lack of filter ) or by another user.
This is consistant with Vantage 6.1.
The result is more records may be marked as buy then expected....
   OperationID: Autoselect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Autoselect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Autoselect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcQtys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcQtys
   Description: This method recalculates RelQty, XRelQty
   OperationID: CalcQtys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcQtys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcQtys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CapableToPromiseGenerate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CapableToPromiseGenerate
   Description: Purpose: Called from bo/CapPromise/CapPromise.p to generate POs
Parameters:  none
Notes:
   OperationID: CapableToPromiseGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CapableToPromiseGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CapableToPromiseGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencySwitch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencySwitch
   Description: Returns the currency display symbol base on currencyswitch.
   OperationID: ChangeCurrencySwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencySwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencySwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailOverridePriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailOverridePriceList
   Description: Run this method when the override pricelist is unchecked
   OperationID: ChangeDetailOverridePriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailOverridePriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOverridePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMfgNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMfgNum
   Description: Called when MfgNum is changed. Updates MfgNumName.
   OperationID: ChangeMfgNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMfgPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMfgPartNum
   Description: Called when MfgNumPart is changed and need to retrieve Supplier Part
   OperationID: ChangeMfgPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePoLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePoLine
   Description: Obsolete method which calls overloaded ChangePoLine
   OperationID: ChangePoLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePoLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePoLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePoLineWithWarning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePoLineWithWarning
   Description: This is called when a PO Line is entered.  An error will return if invalid PO Line, Line is closed, or Part or Configuration is different.
Suggestions fields will be updated with values from PO Line if warnIfDifferences is false, or there are no differences.  Otherwise list of different
fields will be returned in differenceMsg
   OperationID: ChangePoLineWithWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePoLineWithWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePoLineWithWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePoNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePoNum
   Description: This method will change the PoNum and pull in the values associated with the PO Header.
The default fields are; PONum, VendorNum, PurPoint, BuyerID, ShipViaCode, FOB, TermsCode, Name
   OperationID: ChangePoNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePoNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePoNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSugPoMscAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSugPoMscAmt
   Description: Run this method when the amount changes on the ttSugPoMsc .
   OperationID: ChangeSugPoMscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSugPoMscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSugPoMscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSugPoMscCharge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSugPoMscCharge
   Description: Run this method when the poMsc charge changes to default in a description.
   OperationID: ChangeSugPoMscCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSugPoMscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSugPoMscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSugPoMscPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSugPoMscPercent
   Description: Run this method when the percentage changes on the ttSugPoMsc .
   OperationID: ChangeSugPoMscPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSugPoMscPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSugPoMscPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSupplierPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSupplierPart
   Description: Validate that the Supplier part entered exists.
   OperationID: ChangeSupplierPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSupplierPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSupplierPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUnitPriceConfirmOverride(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUnitPriceConfirmOverride
   Description: Checks if the source of the unit price is from a supplier price list, if so
will prompt for confirmation of overriding if flag is set against purchase configuration.
   OperationID: ChangeUnitPriceConfirmOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnitPriceConfirmOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitPriceConfirmOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendor
   Description: This method returns the default information for a vendor. Such as FOB,Terms, purchase point
and currency . This method must be run after changing the VendorID and before invoking the
update method, otherwise all related vendor information on the screen will not be updated.
   OperationID: ChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: ChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBuyers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBuyers
   Description: Need to be run before generating po's, the Generate() method.
            
This method will check to see if generating PO from the currently tagged suggestions will generate
po's for other buyers.
            
Running the Generate method will assume that all tagged suggestion records will generate PO's,
regardless of the buyer.
   OperationID: CheckBuyers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBuyers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBuyers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRelQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRelQty
   Description: Purpose: Called to calculate the RelQty if needed
Parameters:  calcField
Notes:
   OperationID: CheckRelQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRelQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRelQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSugPoDtlCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSugPoDtlCount
   Description: This methods will return a count of NEW PO Suggestions for the selected Buyer
   OperationID: GetSugPoDtlCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSugPoDtlCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugPoDtlCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckGenerate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckGenerate
   Description: This method will check for run out parts and if compliant.
   OperationID: CheckGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateShowCreated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateShowCreated
   Description: This method processes all suggestion records where buy has been set to true within
the passed parameters.
            
This will also return a list of all the purchase order numbers that were generated as part of this run.
            
Note: This is doing a getrows and passing back a new dataset minus the records that
were processed. The dataset at the client will still have the processed records, in
order to removed these records we may have to somehow tag the processed records with
a "D":U or, have the UI replace their dataset with this new one.
   OperationID: GenerateShowCreated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateShowCreated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateShowCreated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Generate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Generate
   Description: This method processes all suggestion records where buy has been set to true within
the passed parameters.
Note: This is doing a getrows and passing back a new dataset minus the records that
were processed. The dataset at the client will still have the processed records, in
order to removed these records we may have to somehow tag the processed records with
a "D":U or, have the UI replace their dataset with this new one.
   OperationID: Generate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Generate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Generate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAuthorizedAgentList(epicorHeaders = None):
   """  
   Summary: Invoke method GetAuthorizedAgentList
   Description: Returns a list of Buyers, authorized for the Current User.
   OperationID: GetAuthorizedAgentList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAuthorizedAgentList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultBuyer(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultBuyer
   Description: Purpose:  RETURNS THE DEFAULT BUYER FOR CURRENT COMPANY
Parameters:  out buyerId, out buyerIdName
Notes:
   OperationID: GetDefaultBuyer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultBuyer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetForecastVendors(epicorHeaders = None):
   """  
   Summary: Invoke method GetForecastVendors
   Description: This method returns a list of inter-company trading partners. Use to populate the
grid to select inter-company partners.
   OperationID: GetForecastVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetForecastVendors_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetListPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListPlant
   Description: Returns a list of rows that satisfy the where clause. Use in place of GetList
   OperationID: GetListPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsPlant
   Description: Returns a dataset containing all rows that satisfy the where clauses. use in place of GetRows
   OperationID: GetRowsPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartIsRunOut(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartIsRunOut
   Description: The method chekcs status of the current Part and if this Part is Active and not onHold
or it`s HoldDay later then today, but it is flagged as Run Out then it sets
value of isRunOut parament in true..
   OperationID: PartIsRunOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartIsRunOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartIsRunOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SendForecast(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SendForecast
   Description: This method will process the selected forecast vendor records and send a forecast.
   OperationID: SendForecast
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SendForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSugPoDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSugPoDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSugPoDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSugPoDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSugPoDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSugPoMsc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSugPoMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSugPoMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSugPoMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSugPoMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SugPoDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SugPoDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPoMscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SugPoMscRow] = obj["value"]
      pass

class Erp_Tablesets_SugPoDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.SugType:str = obj["SugType"]
      """  Type of requirement - "M" - Material "S" - Subcontract.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The Id that links to the Purchasing Agent master file.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the requirement. Not maintainable.  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the requirement.  Not maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job assembly of the requirement.  Not maintainable.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Not maintainable.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.FOB:str = obj["FOB"]
      """  Incoterms  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Defaults from the XASyst.ShipViaCode.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Defaults from the Vendor.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum that ties back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue(Our) Unit Of Measure.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The unit price in the vendors unit of measure.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  The unit price in the vendors unit of measure and currency.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchase UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be copied to the PO detail line. Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.VendorID:str = obj["VendorID"]
      """  Duplicate of Vendor.VendorID. Used for sorting.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  Duplicated from VendorPP.Name. Used for sorting.  """  
      self.Buy:bool = obj["Buy"]
      """  Indicates if this record is to be purchased.  Only records with Buy = Yes will be selected for PO generation.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that this POSugDtl record should be added to.  """  
      self.POLine:int = obj["POLine"]
      """  PO Line # that this POSugDtl record should be added to.   Suggestions that are linked to existing PODetail record will create a new related PORel record.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Duplicated from the Subcontract JobOper.  """  
      self.OrderByDate:str = obj["OrderByDate"]
      """  The date the item needs to be ordered by in order to be received by the Due Date.   DueDate - Lead Time.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected Purchasing lead time (in days). This is used to calculate a suggested "Order By Date" based off the Required Date field.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this POSugDtl record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this POSugDtl record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field can not be blank.  """  
      self.CreateRFQ:bool = obj["CreateRFQ"]
      """  A flag used in PO Suggestions for the user to set if they want to generate an rfq suggestion.  """  
      self.SourceRFQ:bool = obj["SourceRFQ"]
      """  A flag that indicates that this PO Suggestion was created from an RFQ.  This flag is used when running Generate Suggestions - it doesn't delete suggestions flagged as SourceRFQ = YES.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSugNum:int = obj["GlbSugNum"]
      """  Global Suggestion Number identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order suggestions.  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order PO Suggestions.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order PO Suggestions.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  Used only for Buy To Order PO Suggestions.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Order Release flag  """  
      self.SugReason:str = obj["SugReason"]
      """  Reason for suggestion. S=Safety  R= Reorder Z=Zero D=Direct  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related Req (if specified) or Supplier  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  This field along with Company, DemandHeadSeq, DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company, DemandContractNum , DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum,  DemandHeadSeq  and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDtlSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.calcCurrencySwitch:bool = obj["calcCurrencySwitch"]
      self.calcDisplaySymbol:str = obj["calcDisplaySymbol"]
      self.calcDocDisplaySymbol:str = obj["calcDocDisplaySymbol"]
      self.DisablePoFields:bool = obj["DisablePoFields"]
      self.PriceBrkChevron:bool = obj["PriceBrkChevron"]
      self.DisableCurrencySwitch:bool = obj["DisableCurrencySwitch"]
      self.DisablePriceBrkBtn:bool = obj["DisablePriceBrkBtn"]
      self.calcDueDate:str = obj["calcDueDate"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.DisableSRMFields:bool = obj["DisableSRMFields"]
      self.MfgNumName:str = obj["MfgNumName"]
      """  Name of Manufacturer  """  
      self.PartNumTrackDim:bool = obj["PartNumTrackDim"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.ClassDescription:str = obj["ClassDescription"]
      """  Full description of the part class.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.PONUMShipName:str = obj["PONUMShipName"]
      """  defaults from the company file.  """  
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      """  defaults from the company file.  """  
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      """  Ship to contact name.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SugPoDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.SugType:str = obj["SugType"]
      """  Type of requirement - "M" - Material "S" - Subcontract.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The Id that links to the Purchasing Agent master file.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the requirement. Not maintainable.  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the requirement.  Not maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job assembly of the requirement.  Not maintainable.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Not maintainable.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.FOB:str = obj["FOB"]
      """  Incoterms  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Defaults from the XASyst.ShipViaCode.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Defaults from the Vendor.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum that ties back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue(Our) Unit Of Measure.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The unit price in the vendors unit of measure.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  The unit price in the vendors unit of measure and currency.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchase UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be copied to the PO detail line. Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.VendorID:str = obj["VendorID"]
      """  Duplicate of Vendor.VendorID. Used for sorting.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  Duplicated from VendorPP.Name. Used for sorting.  """  
      self.Buy:bool = obj["Buy"]
      """  Indicates if this record is to be purchased.  Only records with Buy = Yes will be selected for PO generation.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that this POSugDtl record should be added to.  """  
      self.POLine:int = obj["POLine"]
      """  PO Line # that this POSugDtl record should be added to.   Suggestions that are linked to existing PODetail record will create a new related PORel record.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Duplicated from the Subcontract JobOper.  """  
      self.OrderByDate:str = obj["OrderByDate"]
      """  The date the item needs to be ordered by in order to be received by the Due Date.   DueDate - Lead Time.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected Purchasing lead time (in days). This is used to calculate a suggested "Order By Date" based off the Required Date field.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this POSugDtl record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this POSugDtl record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field can not be blank.  """  
      self.CreateRFQ:bool = obj["CreateRFQ"]
      """  A flag used in PO Suggestions for the user to set if they want to generate an rfq suggestion.  """  
      self.SourceRFQ:bool = obj["SourceRFQ"]
      """  A flag that indicates that this PO Suggestion was created from an RFQ.  This flag is used when running Generate Suggestions - it doesn't delete suggestions flagged as SourceRFQ = YES.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSugNum:int = obj["GlbSugNum"]
      """  Global Suggestion Number identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order suggestions.  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order PO Suggestions.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order PO Suggestions.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  Used only for Buy To Order PO Suggestions.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Order Release flag  """  
      self.SugReason:str = obj["SugReason"]
      """  Reason for suggestion. S=Safety  R= Reorder Z=Zero D=Direct  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.Per:str = obj["Per"]
      """  Per  """  
      self.ManualFactor:bool = obj["ManualFactor"]
      """  ManualFactor  """  
      self.Factor:int = obj["Factor"]
      """  Factor  """  
      self.PricingQty:int = obj["PricingQty"]
      """  PricingQty  """  
      self.PricingUnitPrice:int = obj["PricingUnitPrice"]
      """  PricingUnitPrice  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.UrgentPlanning:str = obj["UrgentPlanning"]
      """  UrgentPlanning  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MaintainPricingUnits:bool = obj["MaintainPricingUnits"]
      """  MaintainPricingUnits  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related Req (if specified) or Supplier  """  
      self.Review:bool = obj["Review"]
      """  A flag that is set by the user to indicate the suggestion has been reviewed.  This is only used to help filter suggestions.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  This field along with Company, DemandHeadSeq, DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company, DemandContractNum , DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum,  DemandHeadSeq  and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDtlSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created.  """  
      self.calcCurrencySwitch:bool = obj["calcCurrencySwitch"]
      """  If True indicates the Currency matches the Base Currency  """  
      self.calcDocDisplaySymbol:str = obj["calcDocDisplaySymbol"]
      """  Currency symbol in for Document Currency  """  
      self.calcDueDate:str = obj["calcDueDate"]
      self.DisableCurrencySwitch:bool = obj["DisableCurrencySwitch"]
      """  Flag to indicate whether the calcCurrencySwitch field should be disabled.  """  
      self.DisablePoFields:bool = obj["DisablePoFields"]
      self.DisablePriceBrkBtn:bool = obj["DisablePriceBrkBtn"]
      self.DisableSRMFields:bool = obj["DisableSRMFields"]
      self.MfgNumName:str = obj["MfgNumName"]
      """  Name of Manufacturer  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackDim:bool = obj["PartNumTrackDim"]
      self.PriceBrkChevron:bool = obj["PriceBrkChevron"]
      self.calcDisplaySymbol:str = obj["calcDisplaySymbol"]
      """  Currency symbol in for Base Currency  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetAttrClassID:str = obj["DynAttrValueSetAttrClassID"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ManufacturerName:str = obj["ManufacturerName"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PlantName:str = obj["PlantName"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      self.PONUMShipName:str = obj["PONUMShipName"]
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.VendorNumEDISupplier:bool = obj["VendorNumEDISupplier"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.XbSystDisableOverridePriceListOption:bool = obj["XbSystDisableOverridePriceListOption"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SugPoMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overrideable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  If True indicates the Currency matches the Base Currency  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency symbol in for Base Currency  """  
      self.DisableCurrencySwitch:bool = obj["DisableCurrencySwitch"]
      """  Flag to indicate whether the CurrencySwitch field should be disabled.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Currency symbol in for Document Currency  """  
      self.DisableSRMFields:bool = obj["DisableSRMFields"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.SugNumVendorID:str = obj["SugNumVendorID"]
      self.SugNumName:str = obj["SugNumName"]
      self.SugNumLineDesc:str = obj["SugNumLineDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Autoselect_input:
   """ Required : 
   ds
   ipPlantKey
   ipCurBuyer
   ipCutOffDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      self.ipPlantKey:str = obj["ipPlantKey"]
      """  Plant or blank for all  """  
      self.ipCurBuyer:str = obj["ipCurBuyer"]
      """  BuyerId or blank for all buyers  """  
      self.ipCutOffDate:str = obj["ipCutOffDate"]
      """  Cut off date for suggestions  """  
      pass

class Autoselect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalcQtys_input:
   """ Required : 
   calcField
   ds
   """  
   def __init__(self, obj):
      self.calcField:str = obj["calcField"]
      """  calcField  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class CalcQtys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CapableToPromiseGenerate_input:
   """ Required : 
   ipOrderNum
   ipSugNumList
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      self.ipSugNumList:int = obj["ipSugNumList"]
      pass

class CapableToPromiseGenerate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opError:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeCurrencySwitch_input:
   """ Required : 
   currencySwitch
   vendorNum
   currencyCode
   """  
   def __init__(self, obj):
      self.currencySwitch:bool = obj["currencySwitch"]
      """  Logical indicating if the currency toggle is checked  """  
      self.vendorNum:int = obj["vendorNum"]
      """  SugPoDtl.VendorNum  """  
      self.currencyCode:str = obj["currencyCode"]
      """  SugPoDtl.CurrencyCode  """  
      pass

class ChangeCurrencySwitch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.displaySymbol:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDetailOverridePriceList_input:
   """ Required : 
   overridePriceList
   ds
   """  
   def __init__(self, obj):
      self.overridePriceList:bool = obj["overridePriceList"]
      """  True is override pricelist has been checked  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeDetailOverridePriceList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMfgNum_input:
   """ Required : 
   ipMfgNum
   ds
   """  
   def __init__(self, obj):
      self.ipMfgNum:int = obj["ipMfgNum"]
      """  Manufacturer Number  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeMfgNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMfgPartNum_input:
   """ Required : 
   ipMfgPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipMfgPartNum:str = obj["ipMfgPartNum"]
      """  Manufacturer Number  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeMfgPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePoLineWithWarning_input:
   """ Required : 
   newPoLine
   warnIfDifferences
   ds
   """  
   def __init__(self, obj):
      self.newPoLine:int = obj["newPoLine"]
      """  New PO Line to use  """  
      self.warnIfDifferences:bool = obj["warnIfDifferences"]
      """  If True return list of fields that differ between Suggestion and PO Line  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangePoLineWithWarning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      self.differenceMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangePoLine_input:
   """ Required : 
   newPoLine
   ds
   """  
   def __init__(self, obj):
      self.newPoLine:int = obj["newPoLine"]
      """  New Po Line  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangePoLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePoNum_input:
   """ Required : 
   newPoNum
   ds
   """  
   def __init__(self, obj):
      self.newPoNum:int = obj["newPoNum"]
      """  Indicates the Po to retrieve  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangePoNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSugPoMscAmt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeSugPoMscAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSugPoMscCharge_input:
   """ Required : 
   newMiscCode
   ds
   """  
   def __init__(self, obj):
      self.newMiscCode:str = obj["newMiscCode"]
      """  New Misc Code  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeSugPoMscCharge_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSugPoMscPercent_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeSugPoMscPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSupplierPart_input:
   """ Required : 
   newVenPartNum
   ds
   """  
   def __init__(self, obj):
      self.newVenPartNum:str = obj["newVenPartNum"]
      """  The Supplier Part Number proposed value  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeSupplierPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUnitPriceConfirmOverride_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeUnitPriceConfirmOverride_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      self.sConfirmMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeVendor_input:
   """ Required : 
   newVendID
   ds
   """  
   def __init__(self, obj):
      self.newVendID:str = obj["newVendID"]
      """  New Vendor ID  """  
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangeVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class ChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBuyers_input:
   """ Required : 
   opCurBuyer
   """  
   def __init__(self, obj):
      self.opCurBuyer:str = obj["opCurBuyer"]
      """  Current BuyerID  """  
      pass

class CheckBuyers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.poForOtherBuyer:bool = obj["poForOtherBuyer"]
      self.suggList:str = obj["parameters"]
      self.opCurBuyer:str = obj["parameters"]
      self.opBuyerName:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckGenerate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class CheckGenerate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      self.opPartRunOutMessage:str = obj["parameters"]
      self.opComplianceFlag:bool = obj["opComplianceFlag"]
      pass

      """  output parameters  """  

class CheckRelQty_input:
   """ Required : 
   calcField
   """  
   def __init__(self, obj):
      self.calcField:str = obj["calcField"]
      pass

class CheckRelQty_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   sugNum
   """  
   def __init__(self, obj):
      self.sugNum:int = obj["sugNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ForecastVendorsRow:
   def __init__(self, obj):
      self.Send:bool = obj["Send"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendorId:str = obj["VendorId"]
      self.VendorName:str = obj["VendorName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ForecastVendorsTableset:
   def __init__(self, obj):
      self.ForecastVendors:list[Erp_Tablesets_ForecastVendorsRow] = obj["ForecastVendors"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_POSuggTableset:
   def __init__(self, obj):
      self.SugPoDtl:list[Erp_Tablesets_SugPoDtlRow] = obj["SugPoDtl"]
      self.SugPoMsc:list[Erp_Tablesets_SugPoMscRow] = obj["SugPoMsc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SugPoCreatedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PONum:int = obj["PONum"]
      self.VendorID:str = obj["VendorID"]
      self.CreatedDateTime:str = obj["CreatedDateTime"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SugPoCreatedListTableset:
   def __init__(self, obj):
      self.SugPoCreatedList:list[Erp_Tablesets_SugPoCreatedListRow] = obj["SugPoCreatedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SugPoDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.SugType:str = obj["SugType"]
      """  Type of requirement - "M" - Material "S" - Subcontract.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The Id that links to the Purchasing Agent master file.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the requirement. Not maintainable.  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the requirement.  Not maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job assembly of the requirement.  Not maintainable.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Not maintainable.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.FOB:str = obj["FOB"]
      """  Incoterms  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Defaults from the XASyst.ShipViaCode.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Defaults from the Vendor.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum that ties back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue(Our) Unit Of Measure.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The unit price in the vendors unit of measure.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  The unit price in the vendors unit of measure and currency.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchase UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be copied to the PO detail line. Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.VendorID:str = obj["VendorID"]
      """  Duplicate of Vendor.VendorID. Used for sorting.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  Duplicated from VendorPP.Name. Used for sorting.  """  
      self.Buy:bool = obj["Buy"]
      """  Indicates if this record is to be purchased.  Only records with Buy = Yes will be selected for PO generation.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that this POSugDtl record should be added to.  """  
      self.POLine:int = obj["POLine"]
      """  PO Line # that this POSugDtl record should be added to.   Suggestions that are linked to existing PODetail record will create a new related PORel record.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Duplicated from the Subcontract JobOper.  """  
      self.OrderByDate:str = obj["OrderByDate"]
      """  The date the item needs to be ordered by in order to be received by the Due Date.   DueDate - Lead Time.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected Purchasing lead time (in days). This is used to calculate a suggested "Order By Date" based off the Required Date field.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this POSugDtl record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this POSugDtl record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field can not be blank.  """  
      self.CreateRFQ:bool = obj["CreateRFQ"]
      """  A flag used in PO Suggestions for the user to set if they want to generate an rfq suggestion.  """  
      self.SourceRFQ:bool = obj["SourceRFQ"]
      """  A flag that indicates that this PO Suggestion was created from an RFQ.  This flag is used when running Generate Suggestions - it doesn't delete suggestions flagged as SourceRFQ = YES.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSugNum:int = obj["GlbSugNum"]
      """  Global Suggestion Number identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order suggestions.  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order PO Suggestions.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order PO Suggestions.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  Used only for Buy To Order PO Suggestions.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Order Release flag  """  
      self.SugReason:str = obj["SugReason"]
      """  Reason for suggestion. S=Safety  R= Reorder Z=Zero D=Direct  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related Req (if specified) or Supplier  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  This field along with Company, DemandHeadSeq, DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company, DemandContractNum , DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum,  DemandHeadSeq  and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDtlSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.calcCurrencySwitch:bool = obj["calcCurrencySwitch"]
      self.calcDisplaySymbol:str = obj["calcDisplaySymbol"]
      self.calcDocDisplaySymbol:str = obj["calcDocDisplaySymbol"]
      self.DisablePoFields:bool = obj["DisablePoFields"]
      self.PriceBrkChevron:bool = obj["PriceBrkChevron"]
      self.DisableCurrencySwitch:bool = obj["DisableCurrencySwitch"]
      self.DisablePriceBrkBtn:bool = obj["DisablePriceBrkBtn"]
      self.calcDueDate:str = obj["calcDueDate"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.DisableSRMFields:bool = obj["DisableSRMFields"]
      self.MfgNumName:str = obj["MfgNumName"]
      """  Name of Manufacturer  """  
      self.PartNumTrackDim:bool = obj["PartNumTrackDim"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.ClassDescription:str = obj["ClassDescription"]
      """  Full description of the part class.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.PONUMShipName:str = obj["PONUMShipName"]
      """  defaults from the company file.  """  
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      """  defaults from the company file.  """  
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      """  Ship to contact name.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SugPoDtlListTableset:
   def __init__(self, obj):
      self.SugPoDtlList:list[Erp_Tablesets_SugPoDtlListRow] = obj["SugPoDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SugPoDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.SugType:str = obj["SugType"]
      """  Type of requirement - "M" - Material "S" - Subcontract.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The Id that links to the Purchasing Agent master file.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the requirement. Not maintainable.  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the requirement.  Not maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job assembly of the requirement.  Not maintainable.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Not maintainable.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.FOB:str = obj["FOB"]
      """  Incoterms  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Defaults from the XASyst.ShipViaCode.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Defaults from the Vendor.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum that ties back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue(Our) Unit Of Measure.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The unit price in the vendors unit of measure.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  The unit price in the vendors unit of measure and currency.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchase UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be copied to the PO detail line. Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.VendorID:str = obj["VendorID"]
      """  Duplicate of Vendor.VendorID. Used for sorting.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  Duplicated from VendorPP.Name. Used for sorting.  """  
      self.Buy:bool = obj["Buy"]
      """  Indicates if this record is to be purchased.  Only records with Buy = Yes will be selected for PO generation.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that this POSugDtl record should be added to.  """  
      self.POLine:int = obj["POLine"]
      """  PO Line # that this POSugDtl record should be added to.   Suggestions that are linked to existing PODetail record will create a new related PORel record.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Duplicated from the Subcontract JobOper.  """  
      self.OrderByDate:str = obj["OrderByDate"]
      """  The date the item needs to be ordered by in order to be received by the Due Date.   DueDate - Lead Time.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected Purchasing lead time (in days). This is used to calculate a suggested "Order By Date" based off the Required Date field.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this POSugDtl record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this POSugDtl record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field can not be blank.  """  
      self.CreateRFQ:bool = obj["CreateRFQ"]
      """  A flag used in PO Suggestions for the user to set if they want to generate an rfq suggestion.  """  
      self.SourceRFQ:bool = obj["SourceRFQ"]
      """  A flag that indicates that this PO Suggestion was created from an RFQ.  This flag is used when running Generate Suggestions - it doesn't delete suggestions flagged as SourceRFQ = YES.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSugNum:int = obj["GlbSugNum"]
      """  Global Suggestion Number identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to this purchase order suggestion. Used only for Buy To Order suggestions.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order suggestions.  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order PO Suggestions.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order PO Suggestions.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  Used only for Buy To Order PO Suggestions.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Order Release flag  """  
      self.SugReason:str = obj["SugReason"]
      """  Reason for suggestion. S=Safety  R= Reorder Z=Zero D=Direct  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.Per:str = obj["Per"]
      """  Per  """  
      self.ManualFactor:bool = obj["ManualFactor"]
      """  ManualFactor  """  
      self.Factor:int = obj["Factor"]
      """  Factor  """  
      self.PricingQty:int = obj["PricingQty"]
      """  PricingQty  """  
      self.PricingUnitPrice:int = obj["PricingUnitPrice"]
      """  PricingUnitPrice  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.UrgentPlanning:str = obj["UrgentPlanning"]
      """  UrgentPlanning  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MaintainPricingUnits:bool = obj["MaintainPricingUnits"]
      """  MaintainPricingUnits  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related Req (if specified) or Supplier  """  
      self.Review:bool = obj["Review"]
      """  A flag that is set by the user to indicate the suggestion has been reviewed.  This is only used to help filter suggestions.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  This field along with Company, DemandHeadSeq, DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  This field along with Company, DemandContractNum , DemandDtlSeq, and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  This field along with Company, DemandContractNum,  DemandHeadSeq  and DemandScheduleSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  This field along with Company, DemandContractNum, DemandHeadSeq, and DemandDtlSeq make up the unique key to the DemandSchedule record this SugPODtl is linked to.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created.  """  
      self.calcCurrencySwitch:bool = obj["calcCurrencySwitch"]
      """  If True indicates the Currency matches the Base Currency  """  
      self.calcDocDisplaySymbol:str = obj["calcDocDisplaySymbol"]
      """  Currency symbol in for Document Currency  """  
      self.calcDueDate:str = obj["calcDueDate"]
      self.DisableCurrencySwitch:bool = obj["DisableCurrencySwitch"]
      """  Flag to indicate whether the calcCurrencySwitch field should be disabled.  """  
      self.DisablePoFields:bool = obj["DisablePoFields"]
      self.DisablePriceBrkBtn:bool = obj["DisablePriceBrkBtn"]
      self.DisableSRMFields:bool = obj["DisableSRMFields"]
      self.MfgNumName:str = obj["MfgNumName"]
      """  Name of Manufacturer  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackDim:bool = obj["PartNumTrackDim"]
      self.PriceBrkChevron:bool = obj["PriceBrkChevron"]
      self.calcDisplaySymbol:str = obj["calcDisplaySymbol"]
      """  Currency symbol in for Base Currency  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetAttrClassID:str = obj["DynAttrValueSetAttrClassID"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ManufacturerName:str = obj["ManufacturerName"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PlantName:str = obj["PlantName"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      self.PONUMShipName:str = obj["PONUMShipName"]
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.VendorNumEDISupplier:bool = obj["VendorNumEDISupplier"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.XbSystDisableOverridePriceListOption:bool = obj["XbSystDisableOverridePriceListOption"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SugPoMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overrideable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  If True indicates the Currency matches the Base Currency  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency symbol in for Base Currency  """  
      self.DisableCurrencySwitch:bool = obj["DisableCurrencySwitch"]
      """  Flag to indicate whether the CurrencySwitch field should be disabled.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Currency symbol in for Document Currency  """  
      self.DisableSRMFields:bool = obj["DisableSRMFields"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.SugNumVendorID:str = obj["SugNumVendorID"]
      self.SugNumName:str = obj["SugNumName"]
      self.SugNumLineDesc:str = obj["SugNumLineDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPOSuggTableset:
   def __init__(self, obj):
      self.SugPoDtl:list[Erp_Tablesets_SugPoDtlRow] = obj["SugPoDtl"]
      self.SugPoMsc:list[Erp_Tablesets_SugPoMscRow] = obj["SugPoMsc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateShowCreated_input:
   """ Required : 
   ds
   ipPlantKey
   ipCurBuyer
   ipCutOffDate
   sugPoCreatedListDS
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      self.ipPlantKey:str = obj["ipPlantKey"]
      """  Plant or blank for all  """  
      self.ipCurBuyer:str = obj["ipCurBuyer"]
      """  BuyerId or blank for all buyers  """  
      self.ipCutOffDate:str = obj["ipCutOffDate"]
      """  Cut off date for suggestions  """  
      self.sugPoCreatedListDS:list[Erp_Tablesets_SugPoCreatedListTableset] = obj["sugPoCreatedListDS"]
      pass

class GenerateShowCreated_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      self.sugPoCreatedListDS:list[Erp_Tablesets_SugPoCreatedListTableset] = obj["sugPoCreatedListDS"]
      pass

      """  output parameters  """  

class Generate_input:
   """ Required : 
   ds
   ipPlantKey
   ipCurBuyer
   ipCutOffDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      self.ipPlantKey:str = obj["ipPlantKey"]
      """  Plant or blank for all  """  
      self.ipCurBuyer:str = obj["ipCurBuyer"]
      """  BuyerId or blank for all buyers  """  
      self.ipCutOffDate:str = obj["ipCutOffDate"]
      """  Cut off date for suggestions  """  
      pass

class Generate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAuthorizedAgentList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opBuyerName:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   sugNum
   """  
   def __init__(self, obj):
      self.sugNum:int = obj["sugNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POSuggTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POSuggTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POSuggTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDefaultBuyer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.buyerId:str = obj["parameters"]
      self.buyerIdName:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetForecastVendors_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ForecastVendorsTableset] = obj["returnObj"]
      pass

class GetListPlant_input:
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

class GetListPlant_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SugPoDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_SugPoDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSugPoDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class GetNewSugPoDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSugPoMsc_input:
   """ Required : 
   ds
   sugNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      self.sugNum:int = obj["sugNum"]
      pass

class GetNewSugPoMsc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsPlant_input:
   """ Required : 
   whereClauseSugPoDtl
   whereClauseSugPoMsc
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSugPoDtl:str = obj["whereClauseSugPoDtl"]
      """  whereClause for SugPoDtl table  """  
      self.whereClauseSugPoMsc:str = obj["whereClauseSugPoMsc"]
      """  whereClause for SugPoMsc table  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetRowsPlant_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POSuggTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSugPoDtl
   whereClauseSugPoMsc
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSugPoDtl:str = obj["whereClauseSugPoDtl"]
      self.whereClauseSugPoMsc:str = obj["whereClauseSugPoMsc"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POSuggTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSugPoDtlCount_input:
   """ Required : 
   buyerID
   """  
   def __init__(self, obj):
      self.buyerID:str = obj["buyerID"]
      """  buyerID  """  
      pass

class GetSugPoDtlCount_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  Count  """  
      pass

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

class PartIsRunOut_input:
   """ Required : 
   valpartnum
   """  
   def __init__(self, obj):
      self.valpartnum:str = obj["valpartnum"]
      """  The PartNum, whose status need to check  """  
      pass

class PartIsRunOut_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class SendForecast_input:
   """ Required : 
   ds
   ds1
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastVendorsTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_POSuggTableset] = obj["ds1"]
      pass

class SendForecast_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastVendorsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOSuggTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOSuggTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

