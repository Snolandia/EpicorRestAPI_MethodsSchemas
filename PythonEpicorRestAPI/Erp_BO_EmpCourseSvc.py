import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.EmpCourseSvc
# Description: Business object for Employee Training Course Maintenance.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_EmpCourses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpCourses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpCourses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCourseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses",headers=creds) as resp:
           return await resp.json()

async def post_EmpCourses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpCourses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpCourseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpCourseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpCourses_Company_EmpCourseID(Company, EmpCourseID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpCourse item
   Description: Calls GetByID to retrieve the EmpCourse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCourse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpCourseID: Desc: EmpCourseID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpCourseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpCourses_Company_EmpCourseID(Company, EmpCourseID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpCourse for the service
   Description: Calls UpdateExt to update EmpCourse. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpCourse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpCourseID: Desc: EmpCourseID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpCourseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpCourses_Company_EmpCourseID(Company, EmpCourseID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpCourse item
   Description: Call UpdateExt to delete EmpCourse item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpCourse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpCourseID: Desc: EmpCourseID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpCourses_Company_EmpCourseID_EmpCourseAttches(Company, EmpCourseID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EmpCourseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpCourseAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpCourseID: Desc: EmpCourseID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCourseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")/EmpCourseAttches",headers=creds) as resp:
           return await resp.json()

async def get_EmpCourses_Company_EmpCourseID_EmpCourseAttches_Company_EmpCourseID_DrawingSeq(Company, EmpCourseID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpCourseAttch item
   Description: Calls GetByID to retrieve the EmpCourseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCourseAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpCourseID: Desc: EmpCourseID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpCourseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")/EmpCourseAttches(" + Company + "," + EmpCourseID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpCourseAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpCourseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpCourseAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCourseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches",headers=creds) as resp:
           return await resp.json()

async def post_EmpCourseAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpCourseAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpCourseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpCourseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpCourseAttches_Company_EmpCourseID_DrawingSeq(Company, EmpCourseID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpCourseAttch item
   Description: Calls GetByID to retrieve the EmpCourseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCourseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpCourseID: Desc: EmpCourseID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpCourseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches(" + Company + "," + EmpCourseID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpCourseAttches_Company_EmpCourseID_DrawingSeq(Company, EmpCourseID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpCourseAttch for the service
   Description: Calls UpdateExt to update EmpCourseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpCourseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpCourseID: Desc: EmpCourseID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpCourseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches(" + Company + "," + EmpCourseID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpCourseAttches_Company_EmpCourseID_DrawingSeq(Company, EmpCourseID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpCourseAttch item
   Description: Call UpdateExt to delete EmpCourseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpCourseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpCourseID: Desc: EmpCourseID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches(" + Company + "," + EmpCourseID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCourseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseEmpCourse, whereClauseEmpCourseAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseEmpCourse=" + whereClauseEmpCourse
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpCourseAttch=" + whereClauseEmpCourseAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(empCourseID, epicorHeaders = None):
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
   params += "empCourseID=" + empCourseID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CreateMultiRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMultiRequest
   Description: Creates an Employee Course Request for multiple employees.
   OperationID: CreateMultiRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMultiRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMultiRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedEmpCourseCourseStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedEmpCourseCourseStatus
   Description: Invoked after CourseStatus has been changed to update Dates/Costs etc
   OperationID: OnChangedEmpCourseCourseStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedEmpCourseCourseStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedEmpCourseCourseStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingEmpCourseCourseIDRevisionCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingEmpCourseCourseIDRevisionCode
   Description: Invoked on changing of CourseID or RevisionCode
   OperationID: OnChangingEmpCourseCourseIDRevisionCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingEmpCourseCourseIDRevisionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingEmpCourseCourseIDRevisionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingEmpCourseCourseResult(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingEmpCourseCourseResult
   Description: Invoked on change on CourseResult
   OperationID: OnChangingEmpCourseCourseResult
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingEmpCourseCourseResult_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingEmpCourseCourseResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnCourseStatusChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnCourseStatusChanging
   OperationID: OnCourseStatusChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnCourseStatusChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCourseStatusChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEmpID
   Description: ValidateEmpID
   OperationID: ValidateEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCourseStatuses(epicorHeaders = None):
   """  
   Summary: Invoke method GetCourseStatuses
   OperationID: GetCourseStatuses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCourseStatuses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetExpiresOn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExpiresOn
   OperationID: GetExpiresOn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExpiresOn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExpiresOn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRevisionData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRevisionData
   Description: Gets the Description and Duration data for a given course.
   OperationID: GetRevisionData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevisionData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpCourse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpCourse
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpCourse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpCourse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpCourse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpCourseAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpCourseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpCourseAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpCourseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpCourseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpCourseAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpCourseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpCourseRow] = obj["value"]
      pass

class Erp_Tablesets_EmpCourseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpCourseID:int = obj["EmpCourseID"]
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

class Erp_Tablesets_EmpCourseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpCourseID:int = obj["EmpCourseID"]
      """  The technical identifier.  """  
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
      self.CourseStatus:str = obj["CourseStatus"]
      """  The employee course status. Default = R. Possible values: R = Requested, P = Planned, F = Firm, A = Attended.  """  
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
      self.ExpiresOn:str = obj["ExpiresOn"]
      """  Shows when course expires for employee.  """  
      self.CourseIDDescription:str = obj["CourseIDDescription"]
      """  The description of the Training Course.  """  
      self.CourseSchActEndDate:str = obj["CourseSchActEndDate"]
      """  The date that the training course actually ended. This will default to the End Date.  """  
      self.CourseSchActStartDate:str = obj["CourseSchActStartDate"]
      """  The date that the training course actually started. This will default to the Start Date.  """  
      self.EmpIDName:str = obj["EmpIDName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.EmpIDPhone:str = obj["EmpIDPhone"]
      """  Home phone number  """  
      self.RevisionCodeExpiresIn:int = obj["RevisionCodeExpiresIn"]
      """  The number which indicates the expiration period. This will default to 0 which indicates that the training course never expires.  """  
      self.RevisionCodeDurationType:str = obj["RevisionCodeDurationType"]
      """  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  """  
      self.RevisionCodeExpirationType:str = obj["RevisionCodeExpirationType"]
      """  The expiration type. Default = Y. Possible values: M = Months, Y = Years.  """  
      self.RevisionCodeDescription:str = obj["RevisionCodeDescription"]
      """  The description of the training course revision.  """  
      self.RevisionCodeDuration:int = obj["RevisionCodeDuration"]
      """  The duration of the course. When a new revision is created this will default to 1.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpCourseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpCourseID:int = obj["EmpCourseID"]
      """  The technical identifier.  """  
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
      self.CourseStatus:str = obj["CourseStatus"]
      """  The employee course status. Default = R. Possible values: R = Requested, P = Planned, F = Firm, A = Attended.  """  
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
      self.ExpiresOn:str = obj["ExpiresOn"]
      """  Shows when course expires for employee.  """  
      self.Expired:bool = obj["Expired"]
      """  Flag to indicate if the course has expired  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CourseIDDescription:str = obj["CourseIDDescription"]
      self.CourseSchActStartDate:str = obj["CourseSchActStartDate"]
      self.CourseSchActEndDate:str = obj["CourseSchActEndDate"]
      self.EmpIDSupervisorID:str = obj["EmpIDSupervisorID"]
      self.EmpIDPhone:str = obj["EmpIDPhone"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RevisionCodeExpiresIn:int = obj["RevisionCodeExpiresIn"]
      self.RevisionCodeDurationType:str = obj["RevisionCodeDurationType"]
      self.RevisionCodeDescription:str = obj["RevisionCodeDescription"]
      self.RevisionCodeExpirationType:str = obj["RevisionCodeExpirationType"]
      self.RevisionCodeDuration:int = obj["RevisionCodeDuration"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CreateMultiRequest_input:
   """ Required : 
   courseID
   revisionCode
   empIDs
   """  
   def __init__(self, obj):
      self.courseID:str = obj["courseID"]
      """  The course for which the employees are requesting.  """  
      self.revisionCode:str = obj["revisionCode"]
      """  The course's revision.  """  
      self.empIDs:str = obj["empIDs"]
      """  A list of EmpIDs that represent the employees requesting the course.  """  
      pass

class CreateMultiRequest_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   empCourseID
   """  
   def __init__(self, obj):
      self.empCourseID:int = obj["empCourseID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_EmpCourseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpCourseID:int = obj["EmpCourseID"]
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

class Erp_Tablesets_EmpCourseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpCourseID:int = obj["EmpCourseID"]
      """  The technical identifier.  """  
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
      self.CourseStatus:str = obj["CourseStatus"]
      """  The employee course status. Default = R. Possible values: R = Requested, P = Planned, F = Firm, A = Attended.  """  
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
      self.ExpiresOn:str = obj["ExpiresOn"]
      """  Shows when course expires for employee.  """  
      self.CourseIDDescription:str = obj["CourseIDDescription"]
      """  The description of the Training Course.  """  
      self.CourseSchActEndDate:str = obj["CourseSchActEndDate"]
      """  The date that the training course actually ended. This will default to the End Date.  """  
      self.CourseSchActStartDate:str = obj["CourseSchActStartDate"]
      """  The date that the training course actually started. This will default to the Start Date.  """  
      self.EmpIDName:str = obj["EmpIDName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.EmpIDPhone:str = obj["EmpIDPhone"]
      """  Home phone number  """  
      self.RevisionCodeExpiresIn:int = obj["RevisionCodeExpiresIn"]
      """  The number which indicates the expiration period. This will default to 0 which indicates that the training course never expires.  """  
      self.RevisionCodeDurationType:str = obj["RevisionCodeDurationType"]
      """  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  """  
      self.RevisionCodeExpirationType:str = obj["RevisionCodeExpirationType"]
      """  The expiration type. Default = Y. Possible values: M = Months, Y = Years.  """  
      self.RevisionCodeDescription:str = obj["RevisionCodeDescription"]
      """  The description of the training course revision.  """  
      self.RevisionCodeDuration:int = obj["RevisionCodeDuration"]
      """  The duration of the course. When a new revision is created this will default to 1.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpCourseListTableset:
   def __init__(self, obj):
      self.EmpCourseList:list[Erp_Tablesets_EmpCourseListRow] = obj["EmpCourseList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EmpCourseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpCourseID:int = obj["EmpCourseID"]
      """  The technical identifier.  """  
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
      self.CourseStatus:str = obj["CourseStatus"]
      """  The employee course status. Default = R. Possible values: R = Requested, P = Planned, F = Firm, A = Attended.  """  
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
      self.ExpiresOn:str = obj["ExpiresOn"]
      """  Shows when course expires for employee.  """  
      self.Expired:bool = obj["Expired"]
      """  Flag to indicate if the course has expired  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CourseIDDescription:str = obj["CourseIDDescription"]
      self.CourseSchActStartDate:str = obj["CourseSchActStartDate"]
      self.CourseSchActEndDate:str = obj["CourseSchActEndDate"]
      self.EmpIDSupervisorID:str = obj["EmpIDSupervisorID"]
      self.EmpIDPhone:str = obj["EmpIDPhone"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RevisionCodeExpiresIn:int = obj["RevisionCodeExpiresIn"]
      self.RevisionCodeDurationType:str = obj["RevisionCodeDurationType"]
      self.RevisionCodeDescription:str = obj["RevisionCodeDescription"]
      self.RevisionCodeExpirationType:str = obj["RevisionCodeExpirationType"]
      self.RevisionCodeDuration:int = obj["RevisionCodeDuration"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpCourseTableset:
   def __init__(self, obj):
      self.EmpCourse:list[Erp_Tablesets_EmpCourseRow] = obj["EmpCourse"]
      self.EmpCourseAttch:list[Erp_Tablesets_EmpCourseAttchRow] = obj["EmpCourseAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtEmpCourseTableset:
   def __init__(self, obj):
      self.EmpCourse:list[Erp_Tablesets_EmpCourseRow] = obj["EmpCourse"]
      self.EmpCourseAttch:list[Erp_Tablesets_EmpCourseAttchRow] = obj["EmpCourseAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   empCourseID
   """  
   def __init__(self, obj):
      self.empCourseID:int = obj["empCourseID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpCourseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpCourseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpCourseTableset] = obj["returnObj"]
      pass

class GetCourseStatuses_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetExpiresOn_input:
   """ Required : 
   CourseStatus
   CourseID
   RevisionCode
   StartDate
   EndDate
   """  
   def __init__(self, obj):
      self.CourseStatus:str = obj["CourseStatus"]
      self.CourseID:str = obj["CourseID"]
      self.RevisionCode:str = obj["RevisionCode"]
      self.StartDate:str = obj["StartDate"]
      self.EndDate:str = obj["EndDate"]
      pass

class GetExpiresOn_output:
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
      self.returnObj:list[Erp_Tablesets_EmpCourseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEmpCourseAttch_input:
   """ Required : 
   ds
   empCourseID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      self.empCourseID:int = obj["empCourseID"]
      pass

class GetNewEmpCourseAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpCourse_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

class GetNewEmpCourse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRevisionData_input:
   """ Required : 
   CourseID
   RevisionCode
   ds
   """  
   def __init__(self, obj):
      self.CourseID:str = obj["CourseID"]
      self.RevisionCode:str = obj["RevisionCode"]
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

class GetRevisionData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseEmpCourse
   whereClauseEmpCourseAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseEmpCourse:str = obj["whereClauseEmpCourse"]
      self.whereClauseEmpCourseAttch:str = obj["whereClauseEmpCourseAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpCourseTableset] = obj["returnObj"]
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

class OnChangedEmpCourseCourseStatus_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

class OnChangedEmpCourseCourseStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingEmpCourseCourseIDRevisionCode_input:
   """ Required : 
   courseID
   revisionCode
   ds
   """  
   def __init__(self, obj):
      self.courseID:str = obj["courseID"]
      self.revisionCode:str = obj["revisionCode"]
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

class OnChangingEmpCourseCourseIDRevisionCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingEmpCourseCourseResult_input:
   """ Required : 
   reasonCode
   ds
   """  
   def __init__(self, obj):
      self.reasonCode:str = obj["reasonCode"]
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

class OnChangingEmpCourseCourseResult_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnCourseStatusChanging_input:
   """ Required : 
   pcCompany
   pcEmpCourseID
   pcCourseStatus
   pcDeleteCourseSchAttdResponse
   """  
   def __init__(self, obj):
      self.pcCompany:str = obj["pcCompany"]
      self.pcEmpCourseID:int = obj["pcEmpCourseID"]
      self.pcCourseStatus:str = obj["pcCourseStatus"]
      self.pcDeleteCourseSchAttdResponse:str = obj["pcDeleteCourseSchAttdResponse"]
      pass

class OnCourseStatusChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEmpCourseTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEmpCourseTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpCourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateEmpID_input:
   """ Required : 
   EmpID
   """  
   def __init__(self, obj):
      self.EmpID:str = obj["EmpID"]
      pass

class ValidateEmpID_output:
   def __init__(self, obj):
      pass

