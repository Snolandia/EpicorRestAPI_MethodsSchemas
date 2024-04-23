import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FirstArtSvc
# Description: First Article Entry business logic
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FirstArts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FirstArts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FirstArts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FirstArtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts",headers=creds) as resp:
           return await resp.json()

async def post_FirstArts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FirstArts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FirstArtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FirstArtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FirstArt item
   Description: Calls GetByID to retrieve the FirstArt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FirstArt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FirstArtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FirstArt for the service
   Description: Calls UpdateExt to update FirstArt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FirstArt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FirstArtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FirstArt item
   Description: Call UpdateExt to delete FirstArt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FirstArt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_FirstArtAttches(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FirstArtAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FirstArtAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FirstArtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")/FirstArtAttches",headers=creds) as resp:
           return await resp.json()

async def get_FirstArts_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_FirstArtAttches_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_DrawingSeq(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FirstArtAttch item
   Description: Calls GetByID to retrieve the FirstArtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FirstArtAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FirstArtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArts(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + ")/FirstArtAttches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FirstArtAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FirstArtAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FirstArtAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FirstArtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches",headers=creds) as resp:
           return await resp.json()

async def post_FirstArtAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FirstArtAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FirstArtAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FirstArtAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FirstArtAttches_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_DrawingSeq(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FirstArtAttch item
   Description: Calls GetByID to retrieve the FirstArtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FirstArtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FirstArtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FirstArtAttches_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_DrawingSeq(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FirstArtAttch for the service
   Description: Calls UpdateExt to update FirstArtAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FirstArtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FirstArtAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FirstArtAttches_Company_JobNum_AssemblySeq_OprSeq_ResourceID_SeqNum_DrawingSeq(Company, JobNum, AssemblySeq, OprSeq, ResourceID, SeqNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FirstArtAttch item
   Description: Call UpdateExt to delete FirstArtAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FirstArtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/FirstArtAttches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + ResourceID + "," + SeqNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FirstArtListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFirstArt, whereClauseFirstArtAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFirstArt=" + whereClauseFirstArt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFirstArtAttch=" + whereClauseFirstArtAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, assemblySeq, oprSeq, resourceID, seqNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "resourceID=" + resourceID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "seqNum=" + seqNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHistory
   Description: This method takes in the key field values for a First Article, and returns a FirstArtList
dataset of the history of related inspections.
   OperationID: GetHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAssembly
   Description: This method validates the ProposedAssemblySeq, then updates the following assembly-related fields:
FirstArt.JobAsmPartNum
FirstArt.JobAsmRevisionNum
            
This method should be run when the FirstArt.AssemblySeq field changes.
            
An exception is thrown if:
- No Job Assembly exists with the given Assembly Sequence Number
   OperationID: OnChangeAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the pcProposedJobNum, then clears the job-related fields.
FirstArt.JobAsmPartNum
FirstArt.JobAsmRevisionNum
            
This method should be run when the FirstArt.JobNum field changes.
            
An exception is thrown if:
- No Job exists with the given Job Number
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOprSeq
   Description: This method validates the piProposedOprSeq, then updates the operation-related fields.
            
This method should be run when the FirstArt.OprSeq field changes.
            
An exception is thrown if:
- No Job Operation exists with the given OprSeq Number
            
A warning message is returned if there is no First Article quantity set on the Job Operation
   OperationID: OnChangeOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFirstArt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFirstArt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFirstArt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFirstArt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFirstArt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFirstArtAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFirstArtAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFirstArtAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFirstArtAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFirstArtAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FirstArtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FirstArtAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FirstArtListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FirstArtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FirstArtRow] = obj["value"]
      pass

class Erp_Tablesets_FirstArtAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.ResourceID:str = obj["ResourceID"]
      self.SeqNum:int = obj["SeqNum"]
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

class Erp_Tablesets_FirstArtListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this first article transaction applies.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the first article transaction applies to.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  """  
      self.ExpectedQuantity:int = obj["ExpectedQuantity"]
      """  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  An ID of the person who did the first article inspection.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.FAStatus:str = obj["FAStatus"]
      """  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  System date at time inspection time.  """  
      self.ActionTime:int = obj["ActionTime"]
      """  System Time (hr-min-sec) at time of inspection.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the inspection.  """  
      self.InspectedQuantity:int = obj["InspectedQuantity"]
      """  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JobAsmPartNum:str = obj["JobAsmPartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.JobAsmRevisionNum:str = obj["JobAsmRevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields.  """  
      self.FAStatusDescription:str = obj["FAStatusDescription"]
      """  First Article Status Description  """  
      self.DispActionTime:str = obj["DispActionTime"]
      """  Action Time in a Time Format  """  
      self.UOMDesc:str = obj["UOMDesc"]
      """  UOM Code Description  """  
      self.InspectorIDName:str = obj["InspectorIDName"]
      """  Inspector's Full Name.  """  
      self.JobAsmDescription:str = obj["JobAsmDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      """  Full description of Resource.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FirstArtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this first article transaction applies.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the first article transaction applies to.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  """  
      self.ExpectedQuantity:int = obj["ExpectedQuantity"]
      """  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  An ID of the person who did the first article inspection.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.FAStatus:str = obj["FAStatus"]
      """  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  System date at time inspection time.  """  
      self.ActionTime:int = obj["ActionTime"]
      """  System Time (hr-min-sec) at time of inspection.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the inspection.  """  
      self.InspectedQuantity:int = obj["InspectedQuantity"]
      """  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JobAsmPartNum:str = obj["JobAsmPartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.JobAsmRevisionNum:str = obj["JobAsmRevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields.  """  
      self.FAStatusDescription:str = obj["FAStatusDescription"]
      """  First Article Status Description  """  
      self.DispActionTime:str = obj["DispActionTime"]
      """  Action Time in a Time Format  """  
      self.UOMDesc:str = obj["UOMDesc"]
      """  UOM Code Description  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobAsmDescription:str = obj["JobAsmDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   jobNum
   assemblySeq
   oprSeq
   resourceID
   seqNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.resourceID:str = obj["resourceID"]
      self.seqNum:int = obj["seqNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FirstArtAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.ResourceID:str = obj["ResourceID"]
      self.SeqNum:int = obj["SeqNum"]
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

class Erp_Tablesets_FirstArtListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this first article transaction applies.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the first article transaction applies to.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  """  
      self.ExpectedQuantity:int = obj["ExpectedQuantity"]
      """  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  An ID of the person who did the first article inspection.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.FAStatus:str = obj["FAStatus"]
      """  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  System date at time inspection time.  """  
      self.ActionTime:int = obj["ActionTime"]
      """  System Time (hr-min-sec) at time of inspection.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the inspection.  """  
      self.InspectedQuantity:int = obj["InspectedQuantity"]
      """  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JobAsmPartNum:str = obj["JobAsmPartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.JobAsmRevisionNum:str = obj["JobAsmRevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields.  """  
      self.FAStatusDescription:str = obj["FAStatusDescription"]
      """  First Article Status Description  """  
      self.DispActionTime:str = obj["DispActionTime"]
      """  Action Time in a Time Format  """  
      self.UOMDesc:str = obj["UOMDesc"]
      """  UOM Code Description  """  
      self.InspectorIDName:str = obj["InspectorIDName"]
      """  Inspector's Full Name.  """  
      self.JobAsmDescription:str = obj["JobAsmDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      """  Full description of Resource.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FirstArtListTableset:
   def __init__(self, obj):
      self.FirstArtList:list[Erp_Tablesets_FirstArtListRow] = obj["FirstArtList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FirstArtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this first article transaction applies.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the first article transaction applies to.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The sequence of the operation record within the specific Job/Assembly to which this first article transaction applies.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to show which machine created the pieces for first article inspection.  This field may be blank.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the FirstArt record within the Job/AsmSeq/OprSeq/Machine.  Assigned by using last number on file for the Job/AsmSeq/OprSeq/Machine plus 1.  """  
      self.ExpectedQuantity:int = obj["ExpectedQuantity"]
      """  This is the quantity expected to be checked.  This field defaults from the JobOper.FAQty field.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  An ID of the person who did the first article inspection.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is defaulted from the LaborDtl.EmployeeNum or entered manually. It is many not be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.FAStatus:str = obj["FAStatus"]
      """  Can be "W" - Waiting (This is a new record), "A" - Accept, "R" - Resubmit and "P"- Provisional.  Provisional means the operation may be continued but another inspection will be required.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  System date at time inspection time.  """  
      self.ActionTime:int = obj["ActionTime"]
      """  System Time (hr-min-sec) at time of inspection.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the inspection.  """  
      self.InspectedQuantity:int = obj["InspectedQuantity"]
      """  This is the quantity inspected.  This field may be zero only if field FAStatus = "W".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JobAsmPartNum:str = obj["JobAsmPartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.JobAsmRevisionNum:str = obj["JobAsmRevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields.  """  
      self.FAStatusDescription:str = obj["FAStatusDescription"]
      """  First Article Status Description  """  
      self.DispActionTime:str = obj["DispActionTime"]
      """  Action Time in a Time Format  """  
      self.UOMDesc:str = obj["UOMDesc"]
      """  UOM Code Description  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobAsmDescription:str = obj["JobAsmDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FirstArtTableset:
   def __init__(self, obj):
      self.FirstArt:list[Erp_Tablesets_FirstArtRow] = obj["FirstArt"]
      self.FirstArtAttch:list[Erp_Tablesets_FirstArtAttchRow] = obj["FirstArtAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFirstArtTableset:
   def __init__(self, obj):
      self.FirstArt:list[Erp_Tablesets_FirstArtRow] = obj["FirstArt"]
      self.FirstArtAttch:list[Erp_Tablesets_FirstArtAttchRow] = obj["FirstArtAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   assemblySeq
   oprSeq
   resourceID
   seqNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.resourceID:str = obj["resourceID"]
      self.seqNum:int = obj["seqNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FirstArtTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FirstArtTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FirstArtTableset] = obj["returnObj"]
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

class GetHistory_input:
   """ Required : 
   jobNum
   assemblySeq
   oprSeq
   resourceID
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  The Job Number  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  The Job Assembly Sequence  """  
      self.oprSeq:int = obj["oprSeq"]
      """  The Job Operation Sequence  """  
      self.resourceID:str = obj["resourceID"]
      """  The Resource ID  """  
      pass

class GetHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FirstArtListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FirstArtListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFirstArtAttch_input:
   """ Required : 
   ds
   jobNum
   assemblySeq
   oprSeq
   resourceID
   seqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.resourceID:str = obj["resourceID"]
      self.seqNum:int = obj["seqNum"]
      pass

class GetNewFirstArtAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFirstArt_input:
   """ Required : 
   ds
   jobNum
   assemblySeq
   oprSeq
   resourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.resourceID:str = obj["resourceID"]
      pass

class GetNewFirstArt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFirstArt
   whereClauseFirstArtAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFirstArt:str = obj["whereClauseFirstArt"]
      self.whereClauseFirstArtAttch:str = obj["whereClauseFirstArtAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FirstArtTableset] = obj["returnObj"]
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

class OnChangeAssembly_input:
   """ Required : 
   piProposedAssemblySeq
   ds
   """  
   def __init__(self, obj):
      self.piProposedAssemblySeq:int = obj["piProposedAssemblySeq"]
      """  The new proposed Job Assembly value  """  
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

class OnChangeAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   pcProposedJobNum
   ds
   """  
   def __init__(self, obj):
      self.pcProposedJobNum:str = obj["pcProposedJobNum"]
      """  The new proposed Job Number value  """  
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOprSeq_input:
   """ Required : 
   piProposedOprSeq
   ds
   """  
   def __init__(self, obj):
      self.piProposedOprSeq:int = obj["piProposedOprSeq"]
      """  The new proposed Job Operation Sequence value  """  
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

class OnChangeOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcWarningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFirstArtTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFirstArtTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FirstArtTableset] = obj["ds"]
      pass

      """  output parameters  """  

