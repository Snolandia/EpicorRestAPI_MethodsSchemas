import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MktgEvntSvc
# Description: Validates the FromOpCode field and poplutes the From OpCode description.  Is called when
the From Op Code changes.  If the code is not valid, an exception will be thrown.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MktgEvnts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MktgEvnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MktgEvnts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgEvntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvnts",headers=creds) as resp:
           return await resp.json()

async def post_MktgEvnts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MktgEvnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MktgEvntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MktgEvntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvnts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MktgEvnts_Company_MktgCampaignID_MktgEvntSeq(Company, MktgCampaignID, MktgEvntSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MktgEvnt item
   Description: Calls GetByID to retrieve the MktgEvnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MktgEvnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgCampaignID: Desc: MktgCampaignID   Required: True   Allow empty value : True
      :param MktgEvntSeq: Desc: MktgEvntSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MktgEvntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvnts(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MktgEvnts_Company_MktgCampaignID_MktgEvntSeq(Company, MktgCampaignID, MktgEvntSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MktgEvnt for the service
   Description: Calls UpdateExt to update MktgEvnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MktgEvnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgCampaignID: Desc: MktgCampaignID   Required: True   Allow empty value : True
      :param MktgEvntSeq: Desc: MktgEvntSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MktgEvntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvnts(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MktgEvnts_Company_MktgCampaignID_MktgEvntSeq(Company, MktgCampaignID, MktgEvntSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MktgEvnt item
   Description: Call UpdateExt to delete MktgEvnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MktgEvnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgCampaignID: Desc: MktgCampaignID   Required: True   Allow empty value : True
      :param MktgEvntSeq: Desc: MktgEvntSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvnts(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MktgEvnts_Company_MktgCampaignID_MktgEvntSeq_MktgEvntAttches(Company, MktgCampaignID, MktgEvntSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MktgEvntAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MktgEvntAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgCampaignID: Desc: MktgCampaignID   Required: True   Allow empty value : True
      :param MktgEvntSeq: Desc: MktgEvntSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgEvntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvnts(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + ")/MktgEvntAttches",headers=creds) as resp:
           return await resp.json()

async def get_MktgEvnts_Company_MktgCampaignID_MktgEvntSeq_MktgEvntAttches_Company_MktgCampaignID_MktgEvntSeq_DrawingSeq(Company, MktgCampaignID, MktgEvntSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MktgEvntAttch item
   Description: Calls GetByID to retrieve the MktgEvntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MktgEvntAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgCampaignID: Desc: MktgCampaignID   Required: True   Allow empty value : True
      :param MktgEvntSeq: Desc: MktgEvntSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MktgEvntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvnts(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + ")/MktgEvntAttches(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MktgEvntAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MktgEvntAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MktgEvntAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgEvntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvntAttches",headers=creds) as resp:
           return await resp.json()

async def post_MktgEvntAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MktgEvntAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MktgEvntAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MktgEvntAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvntAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MktgEvntAttches_Company_MktgCampaignID_MktgEvntSeq_DrawingSeq(Company, MktgCampaignID, MktgEvntSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MktgEvntAttch item
   Description: Calls GetByID to retrieve the MktgEvntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MktgEvntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgCampaignID: Desc: MktgCampaignID   Required: True   Allow empty value : True
      :param MktgEvntSeq: Desc: MktgEvntSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MktgEvntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvntAttches(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MktgEvntAttches_Company_MktgCampaignID_MktgEvntSeq_DrawingSeq(Company, MktgCampaignID, MktgEvntSeq, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MktgEvntAttch for the service
   Description: Calls UpdateExt to update MktgEvntAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MktgEvntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgCampaignID: Desc: MktgCampaignID   Required: True   Allow empty value : True
      :param MktgEvntSeq: Desc: MktgEvntSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MktgEvntAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvntAttches(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MktgEvntAttches_Company_MktgCampaignID_MktgEvntSeq_DrawingSeq(Company, MktgCampaignID, MktgEvntSeq, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MktgEvntAttch item
   Description: Call UpdateExt to delete MktgEvntAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MktgEvntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgCampaignID: Desc: MktgCampaignID   Required: True   Allow empty value : True
      :param MktgEvntSeq: Desc: MktgEvntSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/MktgEvntAttches(" + Company + "," + MktgCampaignID + "," + MktgEvntSeq + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgEvntListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMktgEvnt, whereClauseMktgEvntAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMktgEvnt=" + whereClauseMktgEvnt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMktgEvntAttch=" + whereClauseMktgEvntAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(mktgCampaignID, mktgEvntSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "mktgCampaignID=" + mktgCampaignID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mktgEvntSeq=" + mktgEvntSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMktgEvnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMktgEvnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMktgEvnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMktgEvnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMktgEvnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMktgEvntAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMktgEvntAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMktgEvntAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMktgEvntAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMktgEvntAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgEvntSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MktgEvntAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MktgEvntAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MktgEvntListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MktgEvntListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MktgEvntRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MktgEvntRow] = obj["value"]
      pass

class Erp_Tablesets_MktgEvntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
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

class Erp_Tablesets_MktgEvntListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  ID of the Marketing Campaign that this event is assigned to.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  A sequence number that uniquely defines the MktgEvnt record within a specific MktgCamp. This is system assigned.  The next available number is determined by reading last MktgEvnt record on the Mktgcamp and then adding ten to it.  """  
      self.ActivityType:str = obj["ActivityType"]
      """  The marketing activity type that is assigned to this marketing event.  """  
      self.EvntDescription:str = obj["EvntDescription"]
      """  Description.  """  
      self.AdvertisementCode:str = obj["AdvertisementCode"]
      """  Marketing Advertisement code associated with this marketing event.  """  
      self.PublicationCode:str = obj["PublicationCode"]
      """  Marketing Publication code associated with this marketing event.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date of the campaign.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date of the campaign.  """  
      self.BudgetCost:int = obj["BudgetCost"]
      """  The total budgeted cost for this marketing event.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  The total actual amount that has been spent for this marketing event.  """  
      self.EstRevenue:int = obj["EstRevenue"]
      """  The estimated value of sales revenue resulting from this marketing event.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not his campaign can be assigned to new leads, opportunities or quotes.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgEvntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  ID of the Marketing Campaign that this event is assigned to.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  A sequence number that uniquely defines the MktgEvnt record within a specific MktgCamp. This is system assigned.  The next available number is determined by reading last MktgEvnt record on the Mktgcamp and then adding ten to it.  """  
      self.ActivityType:str = obj["ActivityType"]
      """  The marketing activity type that is assigned to this marketing event.  """  
      self.EvntDescription:str = obj["EvntDescription"]
      """  Description.  """  
      self.AdvertisementCode:str = obj["AdvertisementCode"]
      """  Marketing Advertisement code associated with this marketing event.  """  
      self.PublicationCode:str = obj["PublicationCode"]
      """  Marketing Publication code associated with this marketing event.  """  
      self.MktgEvntComment:str = obj["MktgEvntComment"]
      """  Comments related to the marketing event.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date of the campaign.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date of the campaign.  """  
      self.BudgetCost:int = obj["BudgetCost"]
      """  The total budgeted cost for this marketing event.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  The total actual amount that has been spent for this marketing event.  """  
      self.EstRevenue:int = obj["EstRevenue"]
      """  The estimated value of sales revenue resulting from this marketing event.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not his campaign can be assigned to new leads, opportunities or quotes.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project ID associated with this marketing event.  """  
      self.ActRevenue:int = obj["ActRevenue"]
      """  The Actual value of sales revenue resulting from this marketing event.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.isDefault:bool = obj["isDefault"]
      """  if Yes, use this record as the default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActivityTypeActivityDescription:str = obj["ActivityTypeActivityDescription"]
      self.AdCodeAdvertDescription:str = obj["AdCodeAdvertDescription"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.PublicationCodePubDescription:str = obj["PublicationCodePubDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   mktgCampaignID
   mktgEvntSeq
   """  
   def __init__(self, obj):
      self.mktgCampaignID:str = obj["mktgCampaignID"]
      self.mktgEvntSeq:int = obj["mktgEvntSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MktgEvntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
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

class Erp_Tablesets_MktgEvntListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  ID of the Marketing Campaign that this event is assigned to.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  A sequence number that uniquely defines the MktgEvnt record within a specific MktgCamp. This is system assigned.  The next available number is determined by reading last MktgEvnt record on the Mktgcamp and then adding ten to it.  """  
      self.ActivityType:str = obj["ActivityType"]
      """  The marketing activity type that is assigned to this marketing event.  """  
      self.EvntDescription:str = obj["EvntDescription"]
      """  Description.  """  
      self.AdvertisementCode:str = obj["AdvertisementCode"]
      """  Marketing Advertisement code associated with this marketing event.  """  
      self.PublicationCode:str = obj["PublicationCode"]
      """  Marketing Publication code associated with this marketing event.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date of the campaign.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date of the campaign.  """  
      self.BudgetCost:int = obj["BudgetCost"]
      """  The total budgeted cost for this marketing event.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  The total actual amount that has been spent for this marketing event.  """  
      self.EstRevenue:int = obj["EstRevenue"]
      """  The estimated value of sales revenue resulting from this marketing event.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not his campaign can be assigned to new leads, opportunities or quotes.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgEvntListTableset:
   def __init__(self, obj):
      self.MktgEvntList:list[Erp_Tablesets_MktgEvntListRow] = obj["MktgEvntList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MktgEvntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  ID of the Marketing Campaign that this event is assigned to.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  A sequence number that uniquely defines the MktgEvnt record within a specific MktgCamp. This is system assigned.  The next available number is determined by reading last MktgEvnt record on the Mktgcamp and then adding ten to it.  """  
      self.ActivityType:str = obj["ActivityType"]
      """  The marketing activity type that is assigned to this marketing event.  """  
      self.EvntDescription:str = obj["EvntDescription"]
      """  Description.  """  
      self.AdvertisementCode:str = obj["AdvertisementCode"]
      """  Marketing Advertisement code associated with this marketing event.  """  
      self.PublicationCode:str = obj["PublicationCode"]
      """  Marketing Publication code associated with this marketing event.  """  
      self.MktgEvntComment:str = obj["MktgEvntComment"]
      """  Comments related to the marketing event.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date of the campaign.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date of the campaign.  """  
      self.BudgetCost:int = obj["BudgetCost"]
      """  The total budgeted cost for this marketing event.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  The total actual amount that has been spent for this marketing event.  """  
      self.EstRevenue:int = obj["EstRevenue"]
      """  The estimated value of sales revenue resulting from this marketing event.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not his campaign can be assigned to new leads, opportunities or quotes.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project ID associated with this marketing event.  """  
      self.ActRevenue:int = obj["ActRevenue"]
      """  The Actual value of sales revenue resulting from this marketing event.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.isDefault:bool = obj["isDefault"]
      """  if Yes, use this record as the default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActivityTypeActivityDescription:str = obj["ActivityTypeActivityDescription"]
      self.AdCodeAdvertDescription:str = obj["AdCodeAdvertDescription"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.PublicationCodePubDescription:str = obj["PublicationCodePubDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgEvntTableset:
   def __init__(self, obj):
      self.MktgEvnt:list[Erp_Tablesets_MktgEvntRow] = obj["MktgEvnt"]
      self.MktgEvntAttch:list[Erp_Tablesets_MktgEvntAttchRow] = obj["MktgEvntAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMktgEvntTableset:
   def __init__(self, obj):
      self.MktgEvnt:list[Erp_Tablesets_MktgEvntRow] = obj["MktgEvnt"]
      self.MktgEvntAttch:list[Erp_Tablesets_MktgEvntAttchRow] = obj["MktgEvntAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   mktgCampaignID
   mktgEvntSeq
   """  
   def __init__(self, obj):
      self.mktgCampaignID:str = obj["mktgCampaignID"]
      self.mktgEvntSeq:int = obj["mktgEvntSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MktgEvntTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MktgEvntTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MktgEvntTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MktgEvntListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMktgEvntAttch_input:
   """ Required : 
   ds
   mktgCampaignID
   mktgEvntSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgEvntTableset] = obj["ds"]
      self.mktgCampaignID:str = obj["mktgCampaignID"]
      self.mktgEvntSeq:int = obj["mktgEvntSeq"]
      pass

class GetNewMktgEvntAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgEvntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMktgEvnt_input:
   """ Required : 
   ds
   mktgCampaignID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgEvntTableset] = obj["ds"]
      self.mktgCampaignID:str = obj["mktgCampaignID"]
      pass

class GetNewMktgEvnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgEvntTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMktgEvnt
   whereClauseMktgEvntAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMktgEvnt:str = obj["whereClauseMktgEvnt"]
      self.whereClauseMktgEvntAttch:str = obj["whereClauseMktgEvntAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MktgEvntTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtMktgEvntTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMktgEvntTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgEvntTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgEvntTableset] = obj["ds"]
      pass

      """  output parameters  """  

