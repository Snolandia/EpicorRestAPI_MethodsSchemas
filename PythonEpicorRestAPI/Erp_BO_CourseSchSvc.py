import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CourseSchSvc
# Description: Course Schedule Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CourseSches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CourseSches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CourseSches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches",headers=creds) as resp:
           return await resp.json()

async def post_CourseSches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CourseSches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseSchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseSchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate(Company, CourseID, RevisionCode, StartDate, EndDate, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseSch item
   Description: Calls GetByID to retrieve the CourseSch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate(Company, CourseID, RevisionCode, StartDate, EndDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CourseSch for the service
   Description: Calls UpdateExt to update CourseSch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CourseSch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseSchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate(Company, CourseID, RevisionCode, StartDate, EndDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CourseSch item
   Description: Call UpdateExt to delete CourseSch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CourseSch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate_CourseSchAttds(Company, CourseID, RevisionCode, StartDate, EndDate, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CourseSchAttds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CourseSchAttds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchAttdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")/CourseSchAttds",headers=creds) as resp:
           return await resp.json()

async def get_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseSchAttd item
   Description: Calls GetByID to retrieve the CourseSchAttd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSchAttd1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CourseSchAttds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CourseSchAttds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CourseSchAttds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchAttdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds",headers=creds) as resp:
           return await resp.json()

async def post_CourseSchAttds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CourseSchAttds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseSchAttd item
   Description: Calls GetByID to retrieve the CourseSchAttd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSchAttd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CourseSchAttd for the service
   Description: Calls UpdateExt to update CourseSchAttd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CourseSchAttd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CourseSchAttd item
   Description: Call UpdateExt to delete CourseSchAttd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CourseSchAttd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_CourseSchAttdAttches(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CourseSchAttdAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CourseSchAttdAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchAttdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")/CourseSchAttdAttches",headers=creds) as resp:
           return await resp.json()

async def get_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_CourseSchAttdAttches_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_DrawingSeq(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseSchAttdAttch item
   Description: Calls GetByID to retrieve the CourseSchAttdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSchAttdAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")/CourseSchAttdAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CourseSchAttdAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CourseSchAttdAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CourseSchAttdAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchAttdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches",headers=creds) as resp:
           return await resp.json()

async def post_CourseSchAttdAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CourseSchAttdAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CourseSchAttdAttches_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_DrawingSeq(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseSchAttdAttch item
   Description: Calls GetByID to retrieve the CourseSchAttdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSchAttdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CourseSchAttdAttches_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_DrawingSeq(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CourseSchAttdAttch for the service
   Description: Calls UpdateExt to update CourseSchAttdAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CourseSchAttdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CourseSchAttdAttches_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_DrawingSeq(Company, CourseID, RevisionCode, StartDate, EndDate, EmpID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CourseSchAttdAttch item
   Description: Call UpdateExt to delete CourseSchAttdAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CourseSchAttdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param StartDate: Desc: StartDate   Required: True   Allow empty value : True
      :param EndDate: Desc: EndDate   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCourseSch, whereClauseCourseSchAttd, whereClauseCourseSchAttdAttch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseCourseSch=" + whereClauseCourseSch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCourseSchAttd=" + whereClauseCourseSchAttd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCourseSchAttdAttch=" + whereClauseCourseSchAttdAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(courseID, revisionCode, startDate, endDate, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "courseID=" + courseID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "revisionCode=" + revisionCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "startDate=" + startDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "endDate=" + endDate

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_InstrTypeChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InstrTypeChanged
   Description: Method to call when changing the InstrType field.
   OperationID: InstrTypeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InstrTypeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InstrTypeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CourseResultChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CourseResultChanged
   Description: Method to call when changing the CourseResult field.
   OperationID: CourseResultChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseResultChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseResultChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CourseSchAttdEmpIDChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CourseSchAttdEmpIDChanging
   Description: Method to call when changing Course Schedule Attendee employee
   OperationID: CourseSchAttdEmpIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseSchAttdEmpIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseSchAttdEmpIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnStartDateChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnStartDateChanging
   Description: Method to call when changing the StartDate field.
   OperationID: OnStartDateChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnStartDateChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnStartDateChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CourseSchEmpIDChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CourseSchEmpIDChanging
   Description: Method to call when changing Course Schedule employee
   OperationID: CourseSchEmpIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseSchEmpIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseSchEmpIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CourseSchSupplierIDChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CourseSchSupplierIDChanging
   Description: Method to call when changing Course Schedule supplier
   OperationID: CourseSchSupplierIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseSchSupplierIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseSchSupplierIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CourseSchCustIDChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CourseSchCustIDChanging
   Description: Method to call when changing Course Schedule customer
   OperationID: CourseSchCustIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseSchCustIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseSchCustIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInstrTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetInstrTypes
   Description: Returns instructor type list
   OperationID: GetInstrTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstrTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AddAttendees(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddAttendees
   Description: The method for assigning employees to the scheduled course.
   OperationID: AddAttendees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddAttendees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddAttendees_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckFreeSpotsForCourseAttendee(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckFreeSpotsForCourseAttendee
   Description: The method for assigning employees to the scheduled course.
   OperationID: CheckFreeSpotsForCourseAttendee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFreeSpotsForCourseAttendee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFreeSpotsForCourseAttendee_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCourseSch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCourseSch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourseSch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourseSch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourseSch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCourseSchAttd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCourseSchAttd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourseSchAttd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourseSchAttd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourseSchAttd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCourseSchAttdAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCourseSchAttdAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourseSchAttdAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourseSchAttdAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourseSchAttdAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CourseSchAttdAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CourseSchAttdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CourseSchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CourseSchRow] = obj["value"]
      pass

class Erp_Tablesets_CourseSchAttdAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CourseID:str = obj["CourseID"]
      self.RevisionCode:str = obj["RevisionCode"]
      self.StartDate:str = obj["StartDate"]
      self.EndDate:str = obj["EndDate"]
      self.EmpID:str = obj["EmpID"]
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

class Erp_Tablesets_CourseSchAttdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The Training Course ID.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The Course Revision Code.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee ID attending the course.  """  
      self.MaterialCost:int = obj["MaterialCost"]
      """  The cost of the training course materials for the employee.  """  
      self.Expenses:int = obj["Expenses"]
      """  The employee's expenses whilst attending the course.  """  
      self.CostReimbursed:bool = obj["CostReimbursed"]
      """  This flag is used to indicate if the expenses have been reimbursed. Setting this field to true does NOT automatically pay the employee expenses.  """  
      self.CourseResult:str = obj["CourseResult"]
      """  This will contain any Reason Code that has a Reason Code Type set to U - Course Result.  """  
      self.Passed:bool = obj["Passed"]
      """  This will default to value defined against the selected Course Result. If no Course Result is selected then this field will be set to false.  """  
      self.Comments:str = obj["Comments"]
      """  The employee training course results comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseSchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The Training Course ID.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The Course Revision Code.  """  
      self.StartDate:str = obj["StartDate"]
      """  The date that the training course is due to start. When a new schedule is created this will default to the current date.  """  
      self.EndDate:str = obj["EndDate"]
      """  The date that the training course will end. This will default to a date that is calculated using the Duration and the Duration Type from the CourseRevision.  """  
      self.ActStartDate:str = obj["ActStartDate"]
      """  The date that the training course actually started. This will default to the Start Date.  """  
      self.ActEndDate:str = obj["ActEndDate"]
      """  The date that the training course actually ended. This will default to the End Date.  """  
      self.Location:str = obj["Location"]
      """  The free format text to describe where the course will take place.  """  
      self.MaxAttendees:int = obj["MaxAttendees"]
      """  The number that specifies the maximum number of attendees. If it is 0 then there is no limit to the number of attendees.  """  
      self.CourseCost:int = obj["CourseCost"]
      """  The cost of the course per employee.  """  
      self.InstrType:str = obj["InstrType"]
      """  The instructor type. Default = E. Possible values: E = Employee, S = Supplier, C = Customer.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee ID. Must be specified if InstrType = E.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier ID. Must be specified if InstrType = S.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer ID. Must be specified if InstrType = C.  """  
      self.Comments:str = obj["Comments"]
      """  The training course schedule comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.EmpIDName:str = obj["EmpIDName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.RevisionCodeDescription:str = obj["RevisionCodeDescription"]
      """  The description of the training course revision.  """  
      self.RevisionCodeDurationType:str = obj["RevisionCodeDurationType"]
      """  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  """  
      self.RevisionCodeDuration:int = obj["RevisionCodeDuration"]
      """  The duration of the course. When a new revision is created this will default to 1.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseSchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The Training Course ID.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The Course Revision Code.  """  
      self.StartDate:str = obj["StartDate"]
      """  The date that the training course is due to start. When a new schedule is created this will default to the current date.  """  
      self.EndDate:str = obj["EndDate"]
      """  The date that the training course will end. This will default to a date that is calculated using the Duration and the Duration Type from the CourseRevision.  """  
      self.ActStartDate:str = obj["ActStartDate"]
      """  The date that the training course actually started. This will default to the Start Date.  """  
      self.ActEndDate:str = obj["ActEndDate"]
      """  The date that the training course actually ended. This will default to the End Date.  """  
      self.Location:str = obj["Location"]
      """  The free format text to describe where the course will take place.  """  
      self.MaxAttendees:int = obj["MaxAttendees"]
      """  The number that specifies the maximum number of attendees. If it is 0 then there is no limit to the number of attendees.  """  
      self.CourseCost:int = obj["CourseCost"]
      """  The cost of the course per employee.  """  
      self.InstrType:str = obj["InstrType"]
      """  The instructor type. Default = E. Possible values: E = Employee, S = Supplier, C = Customer.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee ID. Must be specified if InstrType = E.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier ID. Must be specified if InstrType = S.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer ID. Must be specified if InstrType = C.  """  
      self.Comments:str = obj["Comments"]
      """  The training course schedule comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.RevisionCodeDurationType:str = obj["RevisionCodeDurationType"]
      self.RevisionCodeDuration:int = obj["RevisionCodeDuration"]
      self.RevisionCodeDescription:str = obj["RevisionCodeDescription"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddAttendees_input:
   """ Required : 
   CourseID
   RevisionCode
   StartDate
   EndDate
   EmpCourses
   ds
   """  
   def __init__(self, obj):
      self.CourseID:str = obj["CourseID"]
      """  The Course ID  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The Course Revision ID  """  
      self.StartDate:str = obj["StartDate"]
      """  The Course Start Date  """  
      self.EndDate:str = obj["EndDate"]
      """  The Course End Date  """  
      self.EmpCourses:str = obj["EmpCourses"]
      """  The list of employee records IDs from EmpCourse table  """  
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class AddAttendees_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckFreeSpotsForCourseAttendee_input:
   """ Required : 
   CourseID
   RevisionCode
   StartDate
   EndDate
   NumAttendees
   """  
   def __init__(self, obj):
      self.CourseID:str = obj["CourseID"]
      """  The Course ID  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The Course Revision ID  """  
      self.StartDate:str = obj["StartDate"]
      """  The Course Start Date  """  
      self.EndDate:str = obj["EndDate"]
      """  The Course End Date  """  
      self.NumAttendees:int = obj["NumAttendees"]
      """  The number of attendees to be added to the Scheduled Course  """  
      pass

class CheckFreeSpotsForCourseAttendee_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.roomOK:bool = obj["roomOK"]
      pass

      """  output parameters  """  

class CourseResultChanged_input:
   """ Required : 
   proposedCourseResult
   ds
   """  
   def __init__(self, obj):
      self.proposedCourseResult:str = obj["proposedCourseResult"]
      """  The proposed Course Result  """  
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class CourseResultChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CourseSchAttdEmpIDChanging_input:
   """ Required : 
   proposedEmpID
   ds
   """  
   def __init__(self, obj):
      self.proposedEmpID:str = obj["proposedEmpID"]
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class CourseSchAttdEmpIDChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CourseSchCustIDChanging_input:
   """ Required : 
   proposedCustID
   ds
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class CourseSchCustIDChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CourseSchEmpIDChanging_input:
   """ Required : 
   proposedEmpID
   ds
   """  
   def __init__(self, obj):
      self.proposedEmpID:str = obj["proposedEmpID"]
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class CourseSchEmpIDChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CourseSchSupplierIDChanging_input:
   """ Required : 
   proposedSupplierID
   ds
   """  
   def __init__(self, obj):
      self.proposedSupplierID:str = obj["proposedSupplierID"]
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class CourseSchSupplierIDChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   courseID
   revisionCode
   startDate
   endDate
   """  
   def __init__(self, obj):
      self.courseID:str = obj["courseID"]
      self.revisionCode:str = obj["revisionCode"]
      self.startDate:str = obj["startDate"]
      self.endDate:str = obj["endDate"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CourseSchAttdAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CourseID:str = obj["CourseID"]
      self.RevisionCode:str = obj["RevisionCode"]
      self.StartDate:str = obj["StartDate"]
      self.EndDate:str = obj["EndDate"]
      self.EmpID:str = obj["EmpID"]
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

class Erp_Tablesets_CourseSchAttdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The Training Course ID.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The Course Revision Code.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee ID attending the course.  """  
      self.MaterialCost:int = obj["MaterialCost"]
      """  The cost of the training course materials for the employee.  """  
      self.Expenses:int = obj["Expenses"]
      """  The employee's expenses whilst attending the course.  """  
      self.CostReimbursed:bool = obj["CostReimbursed"]
      """  This flag is used to indicate if the expenses have been reimbursed. Setting this field to true does NOT automatically pay the employee expenses.  """  
      self.CourseResult:str = obj["CourseResult"]
      """  This will contain any Reason Code that has a Reason Code Type set to U - Course Result.  """  
      self.Passed:bool = obj["Passed"]
      """  This will default to value defined against the selected Course Result. If no Course Result is selected then this field will be set to false.  """  
      self.Comments:str = obj["Comments"]
      """  The employee training course results comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseSchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The Training Course ID.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The Course Revision Code.  """  
      self.StartDate:str = obj["StartDate"]
      """  The date that the training course is due to start. When a new schedule is created this will default to the current date.  """  
      self.EndDate:str = obj["EndDate"]
      """  The date that the training course will end. This will default to a date that is calculated using the Duration and the Duration Type from the CourseRevision.  """  
      self.ActStartDate:str = obj["ActStartDate"]
      """  The date that the training course actually started. This will default to the Start Date.  """  
      self.ActEndDate:str = obj["ActEndDate"]
      """  The date that the training course actually ended. This will default to the End Date.  """  
      self.Location:str = obj["Location"]
      """  The free format text to describe where the course will take place.  """  
      self.MaxAttendees:int = obj["MaxAttendees"]
      """  The number that specifies the maximum number of attendees. If it is 0 then there is no limit to the number of attendees.  """  
      self.CourseCost:int = obj["CourseCost"]
      """  The cost of the course per employee.  """  
      self.InstrType:str = obj["InstrType"]
      """  The instructor type. Default = E. Possible values: E = Employee, S = Supplier, C = Customer.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee ID. Must be specified if InstrType = E.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier ID. Must be specified if InstrType = S.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer ID. Must be specified if InstrType = C.  """  
      self.Comments:str = obj["Comments"]
      """  The training course schedule comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.EmpIDName:str = obj["EmpIDName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.RevisionCodeDescription:str = obj["RevisionCodeDescription"]
      """  The description of the training course revision.  """  
      self.RevisionCodeDurationType:str = obj["RevisionCodeDurationType"]
      """  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  """  
      self.RevisionCodeDuration:int = obj["RevisionCodeDuration"]
      """  The duration of the course. When a new revision is created this will default to 1.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseSchListTableset:
   def __init__(self, obj):
      self.CourseSchList:list[Erp_Tablesets_CourseSchListRow] = obj["CourseSchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CourseSchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The Training Course ID.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The Course Revision Code.  """  
      self.StartDate:str = obj["StartDate"]
      """  The date that the training course is due to start. When a new schedule is created this will default to the current date.  """  
      self.EndDate:str = obj["EndDate"]
      """  The date that the training course will end. This will default to a date that is calculated using the Duration and the Duration Type from the CourseRevision.  """  
      self.ActStartDate:str = obj["ActStartDate"]
      """  The date that the training course actually started. This will default to the Start Date.  """  
      self.ActEndDate:str = obj["ActEndDate"]
      """  The date that the training course actually ended. This will default to the End Date.  """  
      self.Location:str = obj["Location"]
      """  The free format text to describe where the course will take place.  """  
      self.MaxAttendees:int = obj["MaxAttendees"]
      """  The number that specifies the maximum number of attendees. If it is 0 then there is no limit to the number of attendees.  """  
      self.CourseCost:int = obj["CourseCost"]
      """  The cost of the course per employee.  """  
      self.InstrType:str = obj["InstrType"]
      """  The instructor type. Default = E. Possible values: E = Employee, S = Supplier, C = Customer.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee ID. Must be specified if InstrType = E.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier ID. Must be specified if InstrType = S.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer ID. Must be specified if InstrType = C.  """  
      self.Comments:str = obj["Comments"]
      """  The training course schedule comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.RevisionCodeDurationType:str = obj["RevisionCodeDurationType"]
      self.RevisionCodeDuration:int = obj["RevisionCodeDuration"]
      self.RevisionCodeDescription:str = obj["RevisionCodeDescription"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseSchTableset:
   def __init__(self, obj):
      self.CourseSch:list[Erp_Tablesets_CourseSchRow] = obj["CourseSch"]
      self.CourseSchAttd:list[Erp_Tablesets_CourseSchAttdRow] = obj["CourseSchAttd"]
      self.CourseSchAttdAttch:list[Erp_Tablesets_CourseSchAttdAttchRow] = obj["CourseSchAttdAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCourseSchTableset:
   def __init__(self, obj):
      self.CourseSch:list[Erp_Tablesets_CourseSchRow] = obj["CourseSch"]
      self.CourseSchAttd:list[Erp_Tablesets_CourseSchAttdRow] = obj["CourseSchAttd"]
      self.CourseSchAttdAttch:list[Erp_Tablesets_CourseSchAttdAttchRow] = obj["CourseSchAttdAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   courseID
   revisionCode
   startDate
   endDate
   """  
   def __init__(self, obj):
      self.courseID:str = obj["courseID"]
      self.revisionCode:str = obj["revisionCode"]
      self.startDate:str = obj["startDate"]
      self.endDate:str = obj["endDate"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CourseSchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CourseSchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CourseSchTableset] = obj["returnObj"]
      pass

class GetInstrTypes_output:
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
      self.returnObj:list[Erp_Tablesets_CourseSchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCourseSchAttdAttch_input:
   """ Required : 
   ds
   courseID
   revisionCode
   startDate
   endDate
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      self.courseID:str = obj["courseID"]
      self.revisionCode:str = obj["revisionCode"]
      self.startDate:str = obj["startDate"]
      self.endDate:str = obj["endDate"]
      self.empID:str = obj["empID"]
      pass

class GetNewCourseSchAttdAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCourseSchAttd_input:
   """ Required : 
   ds
   courseID
   revisionCode
   startDate
   endDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      self.courseID:str = obj["courseID"]
      self.revisionCode:str = obj["revisionCode"]
      self.startDate:str = obj["startDate"]
      self.endDate:str = obj["endDate"]
      pass

class GetNewCourseSchAttd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCourseSch_input:
   """ Required : 
   ds
   courseID
   revisionCode
   startDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      self.courseID:str = obj["courseID"]
      self.revisionCode:str = obj["revisionCode"]
      self.startDate:str = obj["startDate"]
      pass

class GetNewCourseSch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCourseSch
   whereClauseCourseSchAttd
   whereClauseCourseSchAttdAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCourseSch:str = obj["whereClauseCourseSch"]
      self.whereClauseCourseSchAttd:str = obj["whereClauseCourseSchAttd"]
      self.whereClauseCourseSchAttdAttch:str = obj["whereClauseCourseSchAttdAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CourseSchTableset] = obj["returnObj"]
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

class InstrTypeChanged_input:
   """ Required : 
   proposedInstrType
   ds
   """  
   def __init__(self, obj):
      self.proposedInstrType:str = obj["proposedInstrType"]
      """  The proposed Instructor Type  """  
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class InstrTypeChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnStartDateChanging_input:
   """ Required : 
   proposedStartDate
   ds
   """  
   def __init__(self, obj):
      self.proposedStartDate:str = obj["proposedStartDate"]
      """  The proposed Start Date  """  
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class OnStartDateChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCourseSchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCourseSchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseSchTableset] = obj["ds"]
      pass

      """  output parameters  """  

