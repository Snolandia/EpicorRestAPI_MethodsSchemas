import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PriceLstHedSvc
# Description: The PriceLstHed Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstHeds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceLstHeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstHeds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstHeds",headers=creds) as resp:
           return await resp.json()

async def post_PriceLstHeds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstHeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstHeds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceLstHeds_Company_ListCode(Company, ListCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstHed item
   Description: Calls GetByID to retrieve the PriceLstHed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstHeds(" + Company + "," + ListCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceLstHeds_Company_ListCode(Company, ListCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceLstHed for the service
   Description: Calls UpdateExt to update PriceLstHed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstHeds(" + Company + "," + ListCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceLstHeds_Company_ListCode(Company, ListCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceLstHed item
   Description: Call UpdateExt to delete PriceLstHed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstHeds(" + Company + "," + ListCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstHeds_Company_ListCode_PriceLstAttches(Company, ListCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PriceLstAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PriceLstAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstHeds(" + Company + "," + ListCode + ")/PriceLstAttches",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstHeds_Company_ListCode_PriceLstAttches_Company_ListCode_DrawingSeq(Company, ListCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstAttch item
   Description: Calls GetByID to retrieve the PriceLstAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstHeds(" + Company + "," + ListCode + ")/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceLstAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstAttches",headers=creds) as resp:
           return await resp.json()

async def post_PriceLstAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceLstAttches_Company_ListCode_DrawingSeq(Company, ListCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstAttch item
   Description: Calls GetByID to retrieve the PriceLstAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceLstAttches_Company_ListCode_DrawingSeq(Company, ListCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceLstAttch for the service
   Description: Calls UpdateExt to update PriceLstAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceLstAttches_Company_ListCode_DrawingSeq(Company, ListCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceLstAttch item
   Description: Call UpdateExt to delete PriceLstAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePriceLst, whereClausePriceLstAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePriceLst=" + whereClausePriceLst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePriceLstAttch=" + whereClausePriceLstAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(listCode, epicorHeaders = None):
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
   params += "listCode=" + listCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceLst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceLst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceLstAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceLstAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstRow] = obj["value"]
      pass

class Erp_Tablesets_PriceLstAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ListCode:str = obj["ListCode"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.GlobalPriceLst:bool = obj["GlobalPriceLst"]
      """  Marks this PriceLst as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseZeroPrice:bool = obj["UseZeroPrice"]
      """  UseZeroPrice  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.DspWareHouseList:str = obj["DspWareHouseList"]
      self.WareHouseListDescription:str = obj["WareHouseListDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.GlobalPriceLst:bool = obj["GlobalPriceLst"]
      """  Marks this PriceLst as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseZeroPrice:bool = obj["UseZeroPrice"]
      """  UseZeroPrice  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.WareHouseListDescription:str = obj["WareHouseListDescription"]
      """  List of WareHouse descriptions  """  
      self.DspWareHouseList:str = obj["DspWareHouseList"]
      """  Display Ware house list  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.LinkedPriceList_c:str = obj["LinkedPriceList_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   listCode
   """  
   def __init__(self, obj):
      self.listCode:str = obj["listCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PriceLstAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ListCode:str = obj["ListCode"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstHedTableset:
   def __init__(self, obj):
      self.PriceLst:list[Erp_Tablesets_PriceLstRow] = obj["PriceLst"]
      self.PriceLstAttch:list[Erp_Tablesets_PriceLstAttchRow] = obj["PriceLstAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceLstListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.GlobalPriceLst:bool = obj["GlobalPriceLst"]
      """  Marks this PriceLst as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseZeroPrice:bool = obj["UseZeroPrice"]
      """  UseZeroPrice  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.DspWareHouseList:str = obj["DspWareHouseList"]
      self.WareHouseListDescription:str = obj["WareHouseListDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstListTableset:
   def __init__(self, obj):
      self.PriceLstList:list[Erp_Tablesets_PriceLstListRow] = obj["PriceLstList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.GlobalPriceLst:bool = obj["GlobalPriceLst"]
      """  Marks this PriceLst as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseZeroPrice:bool = obj["UseZeroPrice"]
      """  UseZeroPrice  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.WareHouseListDescription:str = obj["WareHouseListDescription"]
      """  List of WareHouse descriptions  """  
      self.DspWareHouseList:str = obj["DspWareHouseList"]
      """  Display Ware house list  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.LinkedPriceList_c:str = obj["LinkedPriceList_c"]
      pass

class Erp_Tablesets_UpdExtPriceLstHedTableset:
   def __init__(self, obj):
      self.PriceLst:list[Erp_Tablesets_PriceLstRow] = obj["PriceLst"]
      self.PriceLstAttch:list[Erp_Tablesets_PriceLstAttchRow] = obj["PriceLstAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   listCode
   """  
   def __init__(self, obj):
      self.listCode:str = obj["listCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstHedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstHedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstHedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPriceLstAttch_input:
   """ Required : 
   ds
   listCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstHedTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      pass

class GetNewPriceLstAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPriceLst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstHedTableset] = obj["ds"]
      pass

class GetNewPriceLst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePriceLst
   whereClausePriceLstAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePriceLst:str = obj["whereClausePriceLst"]
      self.whereClausePriceLstAttch:str = obj["whereClausePriceLstAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstHedTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPriceLstHedTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPriceLstHedTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstHedTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

